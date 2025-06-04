from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
import database.db_connector as db

user_bp = Blueprint("user", __name__, template_folder="../templates/user")


PROFILE_PIC_UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__), "..", "static", "images"
)
PROFILE_PIC_UPLOAD_FOLDER = os.path.abspath(PROFILE_PIC_UPLOAD_FOLDER)


@user_bp.route("/login", methods=["GET", "POST"])
def login_user():
    error = None
    if "user_id" in session:
        return render_template("/homepage.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = __import__("app").app.get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Users WHERE username=%s AND password=%s"
        cursor = db.execute_query(
            conn,
            query=query,
            query_params=(
                username,
                password,
            ),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            print("THIS IS THE USER:", user)
            session["user_id"] = user["user_id"]
            return render_template("/homepage.html")
        else:
            error = "Ran into issues trying to login"
    return render_template("user/login.html", error=error)


@user_bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        skintype = request.form["skintype"]

        conn = __import__("app").app.get_db_connection()

        try:
            cursor = conn.cursor()
            query = " INSERT INTO Users (username, password, email, age, skintype) VALUES (%s, %s, %s, %s, %s) VALUES (?, ?, ?, ?, ?) "
            cursor = db.execute_query(
                conn,
                query=query,
                query_params=(
                    username,
                    password,
                    email,
                    age,
                    skintype,
                ),
            )
            conn.close()

            return redirect(url_for("user.login_user"))

        except db.IntegrityError:
            error = "Username already exists."
        except Exception as e:
            error = f"Registration error: {str(e)}"
            print("❌ Registration Error:", e)

    return render_template("user/register.html", error=error)


@user_bp.route("/")
@user_bp.route("user/profile")
@user_bp.route("/profile", methods=["GET"])
def view_user():
    if "user_id" not in session:
        return redirect("/login")

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    query = (
        "SELECT username, email, age, skintype, profile_pic FROM Users WHERE user_id=%s"
    )
    cursor = db.execute_query(conn, query=query, query_params=(session["user_id"],))
    user = cursor.fetchone()
    conn.close()
    return render_template(
        "user/profile.html",
        user=user,
    )


@user_bp.route("/add", methods=["GET", "POST"])
def add_user():
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    if request.method == "POST":
        # handle form submission...
        pass  # for brevity
    cursor = db.execute_query(
        conn, query="SELECT * FROM Products", query_params=(session["user_id"],)
    )
    products = cursor.fetchall()
    conn.close()
    return render_template("user/add_user.html")


@user_bp.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user_id" not in session:
        return redirect(url_for("user.login_user"))

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    user_id = session["user_id"]

    if request.method == "POST":
        email = request.form.get("email")
        age = request.form.get("age")
        skintype = request.form.get("skintype")

        # Handle image if uploaded
        file = request.files.get("profile_picture")
        if file and file.filename != "":
            filename = secure_filename(file.filename)
            filepath = os.path.join("static/uploads", filename)
            os.makedirs("static/uploads", exist_ok=True)
            file.save(filepath)
            db.execute_query(
                conn,
                query="UPDATE Users SET profile_pic=%s WHERE user_id=%s",
                query_params=(
                    filename,
                    user_id,
                ),
            )

        # Update email, age, and skintype
        db.execute_query(
            conn,
            "UPDATE Users SET email=%s, age=%s, skintype=%s WHERE user_id=%s",
            (
                email,
                age,
                skintype,
                user_id,
            ),
        )

        conn.close()
        return redirect(url_for("user.view_user"))

    cursor = db.execute_query(
        conn,
        "SELECT email, age, skintype, profile_pic FROM Users WHERE user_id=%s",
        (user_id,),
    )
    data = cursor.fetchone()
    conn.close()

    return render_template(
        "user/edit_profile.html",
        user={
            "email": data["email"],
            "age": data["age"],
            "skintype": data["skintype"],
            "picture": data["profile_pic"],
        },
    )


@user_bp.route("/upload_profile_picture", methods=["POST"])
def upload_profile_picture():
    if "user_id" not in session:
        return redirect(url_for("user.login_user"))

    file = request.files.get("profile_picture")
    if file and file.filename != "":
        filename = secure_filename(file.filename)
        filepath = os.path.join(PROFILE_PIC_UPLOAD_FOLDER, filename)
        os.makedirs(PROFILE_PIC_UPLOAD_FOLDER, exist_ok=True)

        # Save the file
        file.save(filepath)

        # Update the database
        conn = __import__("app").app.get_db_connection()
        cursor = conn.cursor()

        db.execute_query(
            conn,
            "UPDATE Users SET profile_pic=? WHERE user_id=%s",
            (
                filename,
                session["user_id"],
            ),
        )
        conn.close()

    return redirect(url_for("user.view_user"))


@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
