from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

diary_bp = Blueprint("diary", __name__, template_folder="../templates/diary")


@diary_bp.route("/")
def view_diary():
    user_id = session.get("user_id", 1)  
    # conn = diary_bp.root_path.split("/routes")[0]
    db = __import__("app").app.get_db_connection()
    entries = db.execute(
        """
        SELECT *, P.product_name
        FROM Diaries D LEFT JOIN Products P ON D.product_id = P.product_id
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

    if request.method == "POST":
        date = request.form["date"]
        product_id = request.form.get("product_id") or None
        body_part = request.form["body_part"]
        acne = 1 if "acne" in request.form else 0
        adverse = 1 if "adverse" in request.form else 0
        diary_note = request.form["diary_note"]

        # Insert into DB
        db = __import__("app").app.get_db_connection()
        entries = db.execute(
            """
            INSERT INTO Diaries (user_id, date, product_id, body_part, acne, adverse, diary_note, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user_id,
                date,
                product_id,
                body_part,
                acne,
                adverse,
                diary_note,
            ),
        )
        db.commit()
        db.close()

        return redirect(url_for("diary"))


    return render_template("add_diary.html")


