from flask import Blueprint, render_template, request, redirect, url_for, session
import os
import datetime
from werkzeug.utils import secure_filename

review_bp = Blueprint("review", __name__, template_folder="../templates/review")


@review_bp.route("/")
@review_bp.route("/all_reviews")
def view_review():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()

    # Get reviews with product names
    reviews = db.execute(
        """
        SELECT R.*, P.product_name
        FROM Reviews R
        LEFT JOIN Products P ON R.product_id = P.product_id
        ORDER BY R.review_id
        """
    ).fetchall()

    # Get shared diary entries with product names
    shared_diaries = db.execute(
        """
        SELECT D.diary_note, D.diary_photo, P.product_name
        FROM Diaries D
        LEFT JOIN Products P ON D.product_id = P.product_id
        WHERE D.shared = 1
        ORDER BY D.date DESC
        """
    ).fetchall()

    db.close()
    return render_template("all_reviews.html", reviews_list=reviews, shared_diaries=shared_diaries)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@review_bp.route("/add/<int:product_id>", methods=["GET", "POST"])
def add_review(product_id):
    if "user_id" not in session:
        return redirect(url_for("user.login"))
    user_id = session["user_id"]

    db = __import__("app").app.get_db_connection()
    product = db.execute(
        "SELECT product_id, product_name, product_pic FROM Products WHERE product_id = ?",
        (product_id,)
    ).fetchone()
    if not product:
        db.close()
        abort(404)

    if request.method == "POST":
        # Process form data
        stars = int(request.form.get('stars', 1))
        review_note = request.form.get('review_note', '').strip()
        repurchase = 1 if request.form.get('repurchase') else 0

        # Photo upload
        photo_file = request.files.get('review_photo')
        filename = None
        if photo_file and allowed_file(photo_file.filename):
            filename = f"review_{user_id}_{product_id}_{int(datetime.datetime.now().timestamp())}_{secure_filename(photo_file.filename)}"
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            photo_file.save(save_path)

        # Insert into database
        db.execute(
            '''
            INSERT INTO Reviews
              (user_id, product_id, stars, review_note, repurchase, review_photo)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (user_id, product_id, stars, review_note, repurchase, filename)
        )
        db.commit()
        db.close()

        return redirect(url_for("product.view_product", product_id=product_id))

    # todays date
    today = datetime.date.today().isoformat()
    db.close()
    return render_template(
        "review_form.html",
        product=product,
        current_date=today
    )
