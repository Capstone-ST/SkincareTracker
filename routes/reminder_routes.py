from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from datetime import datetime
from werkzeug.utils import secure_filename

reminder_bp = Blueprint("reminder", __name__, template_folder="../templates/reminder")

@reminder_bp.route("/reminder")
@reminder_bp.route("/")
def view_reminder():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()
    entries = db.execute(
        """
        SELECT R.*, P.product_name
        FROM Reminders R LEFT JOIN Products P ON R.product_id = P.product_id
        WHERE R.user_id = ?
        ORDER BY R.alarm_date ASC
        """,
        (user_id,),
    ).fetchall()
    db.close()
    return render_template("reminder.html", reminders=entries)

@reminder_bp.route("/reminder/add")
@reminder_bp.route("/add", methods=["GET", "POST"])
def add_reminder():
    user_id = session.get("user_id", 1)

    db = __import__("app").app.get_db_connection()
    products = db.execute("SELECT product_id, product_name FROM Products").fetchall()

    if request.method == "POST":
        reminder_type = request.form["reminder_type"]
        alarm_date = request.form["alarm_date"]
        recurrence = request.form["recurrence"]
        reminder_note = request.form["notes"]
        # user_id = request.form["user_id"]
        product_id = request.form.get("product_id", None)

        db.execute(
            """INSERT INTO Reminders (reminder_type, alarm_date, recurrence, reminder_note, user_id, product_id)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                reminder_type,
                alarm_date,
                recurrence,
                reminder_note,
                user_id,
                product_id if product_id else None,
            ),
        )
        db.commit()
        db.close()
        return redirect("reminder/")

    db.close()
    return render_template("add_reminder.html", products=products)

@reminder_bp.route("/upcoming")
def get_next_upcoming_reminder():
    user_id = session.get("user_id", 1)
    db = __import__("app").app.get_db_connection()
    now = datetime.now().isoformat()

    upcoming = db.execute(
        """
        SELECT R.*, P.product_name FROM Reminders R
        LEFT JOIN Products P ON R.product_id = P.product_id
        WHERE R.user_id = ? AND R.alarm_date >= ?
        ORDER BY R.alarm_date ASC
        LIMIT 1
        """,
        (user_id, now,),
    ).fetchone()
    db.close()
    return render_template("upcoming.html", upcoming=upcoming)

@reminder_bp.route("/delete/<int:id>", methods=["POST"])
def delete_product(id):
    if "user_id" not in session:
        return redirect("/user/login")
    db = __import__("app").app.get_db_connection()
    # Delete from Collections first
    db.execute(
        """
        DELETE FROM Reminders WHERE reminder_id = ?
        """,
        (id),
    )
    db.commit()
    db.close()
    return redirect(url_for("/reminder"))

@reminder_bp.route("/reminder/edit/<int:id>")
@reminder_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_reminder(id):
    db = __import__("app").app.get_db_connection()
    products = db.execute("SELECT product_id, product_name FROM Products").fetchall()

    if request.method == "POST":
        reminder_type = request.form["reminder_type"]
        alarm_date = request.form["alarm_date"]
        recurrence = request.form["recurrence"]
        reminder_note = request.form["notes"]
        product_id = request.form.get("product_id", None)

        db.execute(
            """UPDATE Reminders (reminder_type, alarm_date, recurrence, reminder_note, product_id)
               VALUES (?, ?, ?, ?, ?)
               WHERE reminder_id = ? ;""",
            (
                reminder_type,
                alarm_date,
                recurrence,
                reminder_note,
                product_id if product_id else None,
                id,
            ),
        )
        db.commit()
        db.close()
        return redirect("reminder/")
    
    data = db.execute("SELECT * FROM Reminders WHERE reminder_id=?", (id,)).fetchone()

    db.close()
    return render_template("edit_reminder.html", products=products, data=data)
