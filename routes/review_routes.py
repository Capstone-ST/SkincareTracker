from flask import Blueprint, render_template, request, redirect, url_for, session, abort
import os
import datetime
from werkzeug.utils import secure_filename
import database.db_connector as db

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
UPLOAD_FOLDER = "static/uploads/reviews"
review_bp = Blueprint("review", __name__, template_folder="../templates/review")


@review_bp.route("/")
@review_bp.route("/all_reviews")
def view_review():
    user_id = session.get("user_id", 1)
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    # Get reviews with product names
    reviews_query = "SELECT R.*, P.product_name FROM Reviews R LEFT JOIN Products P ON R.product_id = P.product_id ORDER BY R.review_id"
    cursor = db.execute_query(conn, query=reviews_query, query_params=())
    reviews = cursor.fetchall()

    # Get shared diary entries with product names
    shared_query = "SELECT D.diary_note, D.diary_photo, P.product_name FROM Diaries D LEFT JOIN Products P ON D.product_id = P.product_id WHERE D.shared = 1 ORDER BY D.date DESC"
    cursor = db.execute_query(conn, query=shared_query, query_params=())
    shared_diaries = cursor.fetchall()

    conn.close()
    return render_template(
        "all_reviews.html", reviews_list=reviews, shared_diaries=shared_diaries
    )


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@review_bp.route("/add/<int:product_id>", methods=["GET", "POST"])
def add_review(product_id):
    if "user_id" not in session:
        return redirect(url_for("user.login"))
    user_id = session["user_id"]

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT product_id, product_name, product_pic FROM Products WHERE product_id = %s"

    cursor = db.execute_query(conn, query=query, query_params=(product_id,))
    product = cursor.fetchone()
    if not product:
        conn.close()
        abort(404)

    if request.method == "POST":
        # Process form data
        stars = int(request.form.get("stars", 1))
        review_note = request.form.get("review_note", "").strip()
        repurchase = 1 if request.form.get("repurchase") else 0

        # Photo upload
        photo_file = request.files.get("review_photo")
        filename = None
        if photo_file and allowed_file(photo_file.filename):
            filename = f"review_{user_id}_{product_id}_{int(datetime.datetime.now().timestamp())}_{secure_filename(photo_file.filename)}"
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            photo_file.save(save_path)

        # Insert into database
        query = "INSERT INTO Reviews (user_id, product_id, stars, review_note, repurchase, review_photo) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = db.execute_query(
            conn,
            query,
            (
                user_id,
                product_id,
                stars,
                review_note,
                repurchase,
                filename,
            ),
        )
        conn.close()

        return redirect(url_for("product.view_product", product_id=product_id))

    # todays date
    today = datetime.date.today().isoformat()
    db.close()
    return render_template("review_form.html", product=product, current_date=today)
