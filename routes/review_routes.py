from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

review_bp = Blueprint("review", __name__, template_folder="../templates/review")


@review_bp.route("/")
@review_bp.route("/all_reviews")
def view_review():
    user_id = session.get("user_id", 1)
    # conn = review_bp.root_path.split("/routes")[0]
    db = __import__("app").app.get_db_connection()
    reviews = db.execute(
            """
            SELECT *
            FROM Reviews
            ORDER BY Reviews.review_id
            """,
        ).fetchall()
    print(reviews)
    db.close()
    return render_template("all_reviews.html", reviews_list = reviews)


@review_bp.route("/add", methods=["GET", "POST"])
def add_review():
    user_id = session.get("user_id", 1)

    if request.method == "POST":
        date = request.form["date"]
        product_id = request.form.get("product_id") or None
        body_part = request.form["body_part"]
        acne = 1 if "acne" in request.form else 0
        adverse = 1 if "adverse" in request.form else 0
        review_note = request.form["review_note"]

        # Insert into DB
        db = __import__("app").app.get_db_connection()
        entries = db.execute(
            """
            INSERT INTO Diaries (user_id, date, product_id, body_part, acne, adverse, review_note, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user_id,
                date,
                product_id,
                body_part,
                acne,
                adverse,
                review_note,
            ),
        )
        db.commit()
        db.close()

        return redirect(url_for("review"))

    return render_template("add_review.html")
