from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from flask import jsonify
import requests
from datetime import datetime

home_bp = Blueprint("home", __name__, template_folder="../templates/")


@home_bp.route("/")
@home_bp.route("/homepage")
def view_home():
    if "user_id" not in session:
        return redirect(url_for("user.login_user"))
    upcoming = get_next_upcoming_reminder()
    return render_template("homepage.html", upcoming=upcoming)



@home_bp.route("/collection")
def example():
    return render_template("/homepage.html")

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
        (
            user_id,
            now,
        ),
    ).fetchone()
    db.close()
    return upcoming