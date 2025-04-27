from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from flask import jsonify
import requests

home_bp = Blueprint("/", __name__, template_folder="../templates/")


@home_bp.route("/")
@home_bp.route("/homepage")
def view_home():
    if "user_id" not in session:
        return redirect("/user/login")
    return render_template("/homepage.html")



@home_bp.route("/reminders")
@home_bp.route("/collection")
def example():
    return render_template("/homepage.html")