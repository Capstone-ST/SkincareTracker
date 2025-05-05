from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

user_bp = Blueprint("user", __name__, template_folder="../templates/user")

# cwd = os.getcwd()
# cwd.join("database")
# UPLOAD_FOLDER = cwd.join("images")
# __import__("app").app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# PROFILE_PIC_UPLOAD_FOLDER = __import__("app").app.config["UPLOAD_FOLDER"]
#PROFILE_PIC_UPLOAD_FOLDER = "../database/images/"

PROFILE_PIC_UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "..", "static", "images")
PROFILE_PIC_UPLOAD_FOLDER = os.path.abspath(PROFILE_PIC_UPLOAD_FOLDER)


@user_bp.route("/login", methods=["GET", "POST"])
def login_user():
    error = None
    if "user_id" in session:
        return render_template("/homepage.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = __import__("app").app.get_db_connection()
        user = db.execute(
            "SELECT * FROM Users WHERE username=? AND password=?",
            (username, password),
        ).fetchone()
        db.close()
        if user:
            print("THIS IS THE USER:", user)
            session["user_id"] = user[0]
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
        db = __import__("app").app.get_db_connection()
        try:
            db.execute(
                """
                INSERT INTO Users (username, password, email, age, skintype)
                VALUES (?, ?, ?, ?, ?)
                """,
                (username, password, email, age, skintype),
            )
            db.commit()
            db.close()

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

    db = __import__("app").app.get_db_connection()
    user = db.execute(
        "SELECT username, email, age, skintype, profile_pic FROM Users WHERE user_id=?",
        (session["user_id"],),
    ).fetchone()
    db.close()
    return render_template(
        "user/profile.html",
        user={
            "username": user[0],
            "email": user[1],
            "age": user[2],
            "skintype": user[3],
            "picture": user[4] or 'skincare-user-icon.png'
        },
    )


@user_bp.route("/add", methods=["GET", "POST"])
def add_user():
    db = __import__("app").app.get_db_connection()
    if request.method == "POST":
        # handle form submission...
        pass  # for brevity
    products = db.execute("SELECT * FROM Products").fetchall()
    db.close()
    return render_template("user/add_user.html")


@user_bp.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "user_id" not in session:
        return redirect(url_for("user.login_user"))

    db = __import__("app").app.get_db_connection()
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

            db.execute(
                "UPDATE Users SET profile_pic=? WHERE user_id=?",
                (filename, user_id)
            )

        # Update email, age, and skintype
        db.execute(
            "UPDATE Users SET email=?, age=?, skintype=? WHERE user_id=?",
            (email, age, skintype, user_id)
        )

        db.commit()
        db.close()
        return redirect(url_for("user.view_user"))

    data = db.execute(
        "SELECT email, age, skintype, profile_pic FROM Users WHERE user_id=?",
        (user_id,)
    ).fetchone()
    db.close()

    return render_template(
        "user/edit_profile.html",
        user={
            "email": data[0],
            "age": data[1],
            "skintype": data[2],
            "picture": data[3]
        }
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
        db = __import__("app").app.get_db_connection()
        db.execute(
            "UPDATE Users SET profile_pic=? WHERE user_id=?",
            (filename, session["user_id"]),
        )
        db.commit()
        db.close()

    return redirect(url_for("user.view_user"))



@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
