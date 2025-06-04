from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
import database.db_connector as db

reminder_bp = Blueprint("reminder", __name__, template_folder="../templates/reminder")


@reminder_bp.route("/reminder")
@reminder_bp.route("/")
def view_reminder():
    user_id = session.get("user_id", 1)
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    query = "SELECT R.*, P.product_name FROM Reminders R LEFT JOIN Products P ON R.product_id = P.product_id WHERE R.user_id = %s ORDER BY R.alarm_date ASC"
    cursor = db.execute_query(conn, query=query, query_params=(user_id,))

    entries = cursor.fetchall()
    conn.close()
    return render_template("reminder.html", reminders=entries)


@reminder_bp.route("/reminder/add")
@reminder_bp.route("/add", methods=["GET", "POST"])
def add_reminder():
    user_id = session.get("user_id", 1)

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    cursor = db.execute_query(
        conn, query="SELECT product_id, product_name FROM Products", query_params=()
    )
    products = cursor.fetchall()

    if request.method == "POST":
        reminder_type = request.form["reminder_type"]
        alarm_date = request.form["alarm_date"]
        recurrence = request.form["recurrence"]
        reminder_note = request.form["notes"]
        # user_id = request.form["user_id"]
        product_id = request.form.get("product_id", None)

        query = "INSERT INTO Reminders (reminder_type, alarm_date, recurrence, reminder_note, user_id, product_id) VALUES (%s, %s, %s, %s, %s, %s)"
        query_params = (
            (
                reminder_type,
                alarm_date,
                recurrence,
                reminder_note,
                user_id,
                product_id if product_id else None,
            ),
        )
        cursor = db.execute_query(conn, query=query, query_params=query_params)
        conn.close()
        return redirect("/reminder")

    conn.close()
    return render_template("add_reminder.html", products=products)


@reminder_bp.route("/upcoming")
def get_next_upcoming_reminder():
    user_id = session.get("user_id", 1)
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    now = datetime.now().isoformat()

    query = "SELECT R.*, P.product_name FROM Reminders R LEFT JOIN Products P ON R.product_id = P.product_id WHERE R.user_id = %s AND R.alarm_date >= %s ORDER BY R.alarm_date ASC LIMIT 1"
    query_params = (
        user_id,
        now,
    )
    cursor = db.execute_query(conn, query=query, query_params=query_params)
    upcoming = cursor.fetchone()
    conn.close()
    return render_template("upcoming.html", upcoming=upcoming)


@reminder_bp.route("reminder/delete/<int:id>")
@reminder_bp.route("/delete/<int:id>", methods=["POST"])
def delete_product(id):
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    db.execute_query(
        conn,
        """
        DELETE FROM Reminders WHERE reminder_id = %s
        """,
        (id,),
    )
    conn.close()
    return redirect("/reminder")


@reminder_bp.route("/reminder/edit/<int:id>")
@reminder_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_reminder(id):
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    cursor = db.execute_query(
        conn, query="SELECT product_id, product_name FROM Products", query_params=()
    )
    products = cursor.fetchall()

    if request.method == "POST":
        reminder_type = request.form["reminder_type"]
        alarm_date = request.form["alarm_date"]
        recurrence = request.form["recurrence"]
        reminder_note = request.form["notes"]
        product_id = request.form.get("product_id", None)

        query = "UPDATE Reminders SET reminder_type = %s, alarm_date = %s, recurrence = %s, reminder_note = %s, product_id = %s WHERE reminder_id = %s"
        query_params = (
            reminder_type,
            alarm_date,
            recurrence,
            reminder_note,
            product_id if product_id else None,
            id,
        )
        conn.close()
        return redirect("/reminder")
    query = "SELECT * FROM Reminders WHERE reminder_id=%s"
    cursor = db.execute_query(conn, query=query, query_params=(id,))
    data = cursor.fetchone()

    conn.close()
    return render_template("edit_reminder.html", products=products, data=data)


def days_to_timedelta(days_float: float) -> timedelta:
    total_seconds = days_float * 86400
    return timedelta(seconds=total_seconds)


@reminder_bp.route("/reminder/update/<int:id>")
@reminder_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update_reminder(id):
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM Reminders WHERE reminder_id=%s"
    cursor = db.execute_query(conn, query=query, query_params=(id,))
    data = cursor.fetchone()

    if data["recurrence"] is not None:
        now = datetime.now()
        new_alarm_date = now + days_to_timedelta(data["recurrence"])

        query = "UPDATE Reminders SET alarm_date = %s WHERE reminder_id = %s"
        query_params = (
            new_alarm_date,
            id,
        )
        cursor = db.execute_query(conn, query=query, query_params=query_params)

    else:
        delete_product(id)
    conn.close()
    return redirect("/reminder")
