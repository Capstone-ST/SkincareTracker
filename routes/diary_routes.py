from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv()


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
        time = request.form.get("time", "00:00")
        full_datetime = f"{date} {time}"
        acne = int(request.form.get("acne", 0))
        adverse = 0
        diary_note = request.form.get("notes", "")
        shared = int(request.form.get("shared", 0))
        product_id = int(request.form.get("product_id", None))

        photo = request.files.get("diary_photo")
        photo_filename = None
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join("static/uploads", filename))
            photo_filename = filename

        db.execute(
            """
            INSERT INTO Diaries (user_id, date, product_id, acne, adverse, diary_note, diary_photo, shared)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                full_datetime,
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

@diary_bp.route("/smart_summary", methods=["POST"])
def smart_summary():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()
    entries = db.execute(
        "SELECT diary_note FROM Diaries WHERE user_id = ? ORDER BY date DESC", (user_id,)
    ).fetchall()
    db.close()

    combined_notes = " ".join([entry["diary_note"] for entry in entries if entry["diary_note"]])

    if not combined_notes.strip():
        flash("You don't have enough diary notes for a summary yet.", "warning")
        return redirect(url_for("diary.view_diary"))

    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

        response = llm.invoke([
            SystemMessage(content="You are a helpful skincare assistant."),
            HumanMessage(content=f"Summarize the following skincare diary entries and give one skincare tip:\n\n{combined_notes}")
        ])

        flash(response.content, "info")

    except Exception as e:
        flash(f"AI summary failed: {str(e)}", "danger")

    return redirect(url_for("diary.view_diary"))

@diary_bp.route("/edit/<int:diary_id>", methods=["GET", "POST"])
def edit_diary(diary_id):
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()

    if request.method == "POST":
        date = request.form["date"]
        time = request.form.get("time", "00:00")
        full_datetime = f"{date} {time}"
        acne = int(request.form.get("acne", 0))
        diary_note = request.form.get("notes", "")
        shared = int(request.form.get("shared", 0))
        product_id = int(request.form.get("product_id", 0))

        photo = request.files.get("diary_photo")
        photo_filename = None
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join("static/uploads", filename))
            photo_filename = filename
            db.execute(
                """
                UPDATE Diaries
                SET date = ?, product_id = ?, acne = ?, diary_note = ?, shared = ?, diary_photo = ?
                WHERE diary_id = ? AND user_id = ?
                """,
                (full_datetime, product_id, acne, diary_note, shared, photo_filename, diary_id, user_id)
            )
        else:
            db.execute(
                """
                UPDATE Diaries
                SET date = ?, product_id = ?, acne = ?, diary_note = ?, shared = ?
                WHERE diary_id = ? AND user_id = ?
                """,
                (full_datetime, product_id, acne, diary_note, shared, diary_id, user_id)
            )

        db.commit()
        db.close()
        return redirect(url_for("diary.view_diary"))


    entry = db.execute(
        "SELECT * FROM Diaries WHERE diary_id = ? AND user_id = ?",
        (diary_id, user_id)
    ).fetchone()
    products = db.execute(
        "SELECT product_id, product_name FROM Products WHERE user_id IS NULL OR user_id = ?", (user_id,)
    ).fetchall()
    db.close()

    return render_template("add_diary.html", products=products, entry=entry)

@diary_bp.route("/delete/<int:diary_id>", methods=["POST"])
def delete_diary(diary_id):
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()
    db.execute(
        "DELETE FROM Diaries WHERE diary_id = ? AND user_id = ?",
        (diary_id, user_id)
    )
    db.commit()
    db.close()
    flash("Diary entry deleted.", "info")
    return redirect(url_for("diary.view_diary"))


