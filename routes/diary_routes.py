from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

diary_bp = Blueprint("diary", __name__, template_folder="../templates/diary")

@diary_bp.route("/")
def view_diary():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()
    entries = db.execute(
        """
        SELECT D.*, P.product_name
        FROM Diaries D
        LEFT JOIN Products P ON D.product_id = P.product_id
        WHERE D.user_id = ?
        ORDER BY D.date DESC
        """,
        (user_id,),
    ).fetchall()
    db.close()
    return render_template("diary.html", diary_entries=entries)



@diary_bp.route("/add", methods=["GET", "POST"])
def add_diary():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()

    if request.method == "POST":
        date = request.form["date"]
        acne = int(request.form.get("acne", 0))
        adverse = 0  
        diary_note = request.form.get("notes", "")
        shared = int(request.form.get("shared", 0))
        product_id = int(request.form.get("product_id", None))  

        photo_filename = None 
        db.execute(
            """
            INSERT INTO Diaries (user_id, date, product_id, acne, adverse, diary_note, diary_photo, shared)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                date,
                product_id,
                acne,
                adverse,
                diary_note,
                photo_filename,
                shared, 
            ),
        )
        db.commit()
        db.close()

        return redirect(url_for("diary.view_diary"))

    products = db.execute(
        "SELECT product_id, product_name FROM Products WHERE user_id IS NULL OR user_id = ?", (user_id,)
    ).fetchall()
    db.close()

    return render_template("add_diary.html", products=products)
