import os
import sqlite3
from flask import jsonify
import requests
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

import database

import templates.product.appProduct as appProduct
import templates.user.appUser as appUser




st_db = "skincare.db"  # short for skintracker database

# conn = database.db_connecter.connect_to_database(st_db)

app = Flask(__name__)
app.secret_key = "secret_key"
UPLOAD_FOLDER = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Simulated product database
product_data = {
    "Cerave Moisturizing Cream": {
        "type": "Moisturizer",
        "amazon_link": "https://www.amazon.com/CeraVe-Moisturizing-Moisturizer-Niacinamide-Comedogenic/dp/B0CTTDLQF3/ref=sr_1_10?dib=eyJ2IjoiMSJ9.7orYTXdgOhWduRzEmj8bg5O48rW_SUUDgZasDi-RUmIr9_bqJWIYT-nEtbzwAway31FIkRhyUgW2zZh6cqtnGeftdRGZoqtbIWH_6u-h3yXxvZBDoeN-qiF3hyagEyZw-KU5CKoYUcDv_-cBSDMLirmRMj-F9GzBG77mtmRbqvDJ8VgyekXLZk8-Ad3UszxvYrPg1kIlFfKNrvHXr1awlPxTvULppqJE2owEgmcN8wVJT4fuVl9HgEIhsmxCi68FrjF92fGi2WWzKHa69OoCyiA4z66bX6cajMzszIuA_6c.oXCe0wC75WMJnj7Lr67py-x1X2RS0S0AIYDeFat2HDw&dib_tag=se&keywords=cerave+daily+moisturizing+lotion&qid=1745268145&sr=8-10",
        "directions": "Apply to face and body as needed.",
        "shelf_life": "18 months",
        "ingredients": "Water, Ceramides, Glycerin",
        "image": "cerave.jpeg",
    },
    "Cerave Facial Moisturizing Lotion SPF 30": {
        "type": "Sunscreen",
        "amazon_link": "https://www.amazon.com/CeraVe-Moisturizing-Cream-Daily-Moisturizer/dp/B00TTD9BRC/ref=sr_1_5?crid=3JAIJT4ITK4FW&dib=eyJ2IjoiMSJ9.j7IYE0WXjFEUyEP4FpoxoLBhj0s6oEGXsay5eHgv9eoVhNfnTYboImXGHu-qYRFSQn6anJ8UvQspR8PTErxr2L2dGJq1lddufuAThTMl_3qA9iLABWEP1nMz9n4oKAFVWD5ioeZtrpjf93WE9qn-pahiU2x8s_1mc4I3wL1rkqwtbPdZaSw9S9lxROXCzPLR3EjsbIugXA4X60eRi1HPs9ApcYKJ6clOX-PduEHWgrHrURw0SHsdZrvorlBcYF1xVCCHU7SNX2CsgkemypgCCBOCBZZLOdV4NeeDM8TjGCo.fTMnliWZcekReiH5My1AW2k6pGemFafltkoRlQEFMvs&dib_tag=se&keywords=cerave%2Bdaily%2Bmoisturizing%2Bcream&qid=1745268178&sprefix=cerave%2Bdaily%2Bmoisturizing%2Bcre%2Caps%2C168&sr=8-5&th=1",
        "directions": "Apply 15 minutes before sun exposure.",
        "shelf_life": "12 months",
        "ingredients": "Water, Zinc Oxide, Ceramides",
        "image": "ceravedailysunscreen.jpeg",
    },
}


# Simulated INCIdecoder ingredient database
ingredient_database = {
    "niacinamide": {
        "type": "Serum",
        "amazon_link": "https://www.amazon.com/dp/B079DFPZPJ",
        "directions": "Apply morning and night",
        "shelf_life": "12",
        "ingredients": "Niacinamide, Zinc PCA, Water",
    },
    "salicylic acid": {
        "type": "Cleanser",
        "amazon_link": "https://www.amazon.com/dp/B00LW2GM84",
        "directions": "Use in evening",
        "shelf_life": "9",
        "ingredients": "Salicylic Acid, Glycerin, Water",
    },
}


#  DB Initialization
def init_db():
    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT,
                age INTEGER,
                skintype TEXT,
                picture TEXT DEFAULT 'default.png'
            )
        """)
        # Products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                name TEXT,
                type TEXT,
                amazon_link TEXT,
                directions TEXT,
                shelf_life TEXT,
                ingredients TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(user_id)
            )
        """)

        # Diary table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Diary (
                diary_id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_date TEXT NOT NULL,
                entry_time TEXT,
                products TEXT,
                acne BOOLEAN,
                notes TEXT,
                shared BOOLEAN
    );
        """)

        # Diary Products table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diary_products (
                diary_id INTEGER,
                product_id INTEGER,
                PRIMARY KEY (diary_id, product_id),
                FOREIGN KEY (diary_id) REFERENCES diary(id) ON DELETE CASCADE,
                FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
    );
        """)

        conn.commit()


@app.route("/")
def index():
    return redirect("/homepage")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        session["user_id"] = appUser.login_user(session, error=error)
        return render_template("/homepage.html")
    return render_template("/user/login.html", error=error)




@app.route("/homepage")
def homepage():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("/homepage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        age = request.form["age"]
        skintype = request.form["skintype"]

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO Users (username, password, email, age, skintype)
                    VALUES (?, ?, ?, ?, ?)
                """,
                    (username, password, email, age, skintype),
                )
                conn.commit()
                return redirect("/login")
            except sqlite3.IntegrityError:
                error = "Username already exists."

    return render_template("/user/register.html", error=error)


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/login")
    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username, email, age, skintype, picture FROM Users WHERE user_id=?",
            (session["user_id"],),
        )
        user = cursor.fetchone()
    return render_template(
        "/user/profile.html",
        user={
            "username": user[0],
            "email": user[1],
            "age": user[2],
            "skintype": user[3],
            "picture": user[4],
        },
    )


@app.route("/diary")
def diary():
    if "user_id" not in session:
        return redirect("/login")
    user_id = session.get("user_id", 1)  # Replace with your auth system

    # conn = get_db_connection()
    # diary_entries = conn.execute(
    #     """
    #     SELECT D.*, P.product_name
    #     FROM Diaries D
    #     LEFT JOIN Products P ON D.product_id = P.product_id
    #     WHERE D.user_id = ?
    #     ORDER BY D.date DESC
    # """,
    #     (user_id,),
    # ).fetchall()
    # conn.close()

    # return render_template("/diary/diary.html", diary_entries=diary_entries)
    return render_template("/diary/diary.html")

@app.route("/add_diary", methods=["GET", "POST"])
def add_diary():
    user_id = session.get("user_id", 1)  # Replace with your user logic

    if request.method == "POST":
        date = request.form["date"]
        product_id = request.form.get("product_id") or None
        body_part = request.form["body_part"]
        acne = 1 if "acne" in request.form else 0
        adverse = 1 if "adverse" in request.form else 0
        diary_note = request.form["diary_note"]

    #     photo_filename = None
    #     if "photo" in request.files:
    #         file = request.files["photo"]
    #         if file and allowed_file(file.filename):
    #             filename = secure_filename(file.filename)
    #             photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    #             file.save(photo_path)
    #             photo_filename = filename

    #     # Insert into DB
    #     conn = get_db_connection()
    #     conn.execute(
    #         """
    #         INSERT INTO Diaries (user_id, date, product_id, body_part, acne, adverse, diary_note, photo)
    #         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    #     """,
    #         (
    #             user_id,
    #             date,
    #             product_id,
    #             body_part,
    #             acne,
    #             adverse,
    #             diary_note,
    #             photo_filename,
    #         ),
    #     )
    #     conn.commit()
    #     conn.close()

    #     return redirect(url_for("diary"))

    # # GET: load available products
    # conn = get_db_connection()
    # products = conn.execute("SELECT product_id, product_name FROM Products").fetchall()
    # conn.close()

    return render_template("add_diary.html", products=products)


@app.route("/all_products")
def all_products():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("/product/all_products.html")


@app.route("/product/<product_name>")
def product_info(product_name):
    product = product_data.get(product_name)
    return render_template(
        "/product/product_info.html", product_name=product_name, product=product
    )


@app.route("/product/<product_name>/review", methods=["GET", "POST"])
def write_review(product_name):
    if request.method == "POST":
        review_text = request.form.get("review")
        print(f"Review for {product_name}: {review_text}")
        return redirect(url_for("product_info", product_name=product_name))

    product = product_data.get(product_name)
    return render_template(
        "review/review_form.html", product_name=product_name, product=product
    )


@app.route("/upload-profile-picture", methods=["POST"])
def upload_profile_picture():
    if "user_id" not in session:
        return redirect("/login")
    file = request.files.get("profile_picture")
    if file and file.filename != "":
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Users SET picture=? WHERE user_id=?",
                (filename, session["user_id"]),
            )
            conn.commit()
    return redirect("/profile")


@app.route("/edit-profile", methods=["GET", "POST"])
def edit_profile():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        email = request.form.get("email")
        age = request.form.get("age")
        skintype = request.form.get("skintype")

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE Users SET email=?, age=?, skintype=?
                WHERE user_id=?
            """,
                (email, age, skintype, session["user_id"]),
            )
            conn.commit()
        return redirect("/profile")

    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        #  Add picture here
        cursor.execute(
            "SELECT email, age, skintype, picture FROM Users WHERE user_id=?",
            (session["user_id"],),
        )
        data = cursor.fetchone()

    return render_template(
        "/user/edit_profile.html",
        user={
            "email": data[0],
            "age": data[1],
            "skintype": data[2],
            "picture": data[3],
        },
    )


@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session:
        return redirect("/login")

    product_id = request.args.get("id")

    if request.method == "POST":
        name = request.form.get("name")
        product_type = request.form.get("type")
        amazon_link = request.form.get("amazon_link")
        directions = request.form.get("directions")
        shelf_life = request.form.get("shelf_life")
        ingredients = request.form.get("ingredients")

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            if product_id:
                cursor.execute(
                    """
                    UPDATE Products SET name=?, type=?, amazon_link=?, directions=?, shelf_life=?, ingredients=?
                    WHERE product_id=? AND user_id=?
                """,
                    (
                        name,
                        product_type,
                        amazon_link,
                        directions,
                        shelf_life,
                        ingredients,
                        product_id,
                        session["user_id"],
                    ),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO Products (user_id, name, type, amazon_link, directions, shelf_life, ingredients)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    (
                        session["user_id"],
                        name,
                        product_type,
                        amazon_link,
                        directions,
                        shelf_life,
                        ingredients,
                    ),
                )
            conn.commit()
        return redirect("/products")

    product_data = {}
    if product_id:
        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT name, type, amazon_link, directions, shelf_life, ingredients 
                FROM Products 
                WHERE product_id=? AND user_id=?
            """,
                (product_id, session["user_id"]),
            )
            row = cursor.fetchone()
            if row:
                product_data = {
                    "name": row[0],
                    "type": row[1],
                    "amazon_link": row[2],
                    "directions": row[3],
                    "shelf_life": row[4],
                    "ingredients": row[5],
                }

    return render_template(
        "/product/add_product.html", product=product_data, editing_id=product_id
    )


@app.route("/delete-product/<int:id>", methods=["POST"])
def delete_product(id):
    if "user_id" not in session:
        return redirect("/login")

    try:
        with sqlite3.connect("skincare.db", isolation_level=None) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA busy_timeout = 5000")
            cursor.execute(
                "DELETE FROM Products WHERE product_id=? AND user_id=?",
                (id, session["user_id"]),
            )
    except sqlite3.OperationalError as e:
        return f"Database error: {e}", 500

    return redirect("/products")


@app.route("/api/featured-products")
def featured_products():
    response = requests.get(
        "https://world.openbeautyfacts.org/cgi/search.pl",
        params={
            "search_terms": "skincare",
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "page_size": 20,
        },
    )
    data = response.json()
    products = []

    for product in data.get("products", []):
        name = product.get("product_name_en") or product.get("product_name")
        ingredients = product.get("ingredients_text_en") or product.get(
            "ingredients_text"
        )
        image = product.get("image_front_url", "")

        if name and ingredients and image:
            products.append({"name": name, "image": image, "ingredients": ingredients})

        if len(products) == 5:
            break

    return jsonify(products)


def extract_type_from_categories(categories):
    if not categories:
        return "Unknown"

    categories = categories.lower()
    if "serum" in categories:
        return "Serum"
    if "moisturizer" in categories or "moisturising" in categories:
        return "Moisturizer"
    if "cleanser" in categories or "face-wash" in categories:
        return "Cleanser"
    if "toner" in categories:
        return "Toner"
    if "sunscreen" in categories or "sun-protection" in categories:
        return "Sunscreen"
    if "eye" in categories:
        return "Eye Cream"
    return "Other"


@app.route("/api/get-product-info", methods=["POST"])
def get_product_info():
    product_name = request.form.get("name")
    if not product_name:
        return jsonify({"error": "Missing product name"}), 400

    try:
        response = requests.get(
            "https://world.openbeautyfacts.org/cgi/search.pl",
            params={
                "search_terms": product_name,
                "search_simple": 1,
                "action": "process",
                "json": 1,
                "lc": "en",
                "page_size": 10,
            },
        )
        data = response.json()
        products = data.get("products", [])

        english_product = None
        for p in products:
            if (
                p.get("ingredients_text_en")
                or p.get("product_name_en")
                or p.get("lang") == "en"
            ):
                english_product = p
                break

        if not english_product:
            return jsonify({"error": "No English product found"}), 404

        result = {
            "type": extract_type_from_categories(english_product.get("categories", "")),
            "amazon_link": "#",
            "directions": "N/A",
            "shelf_life": "6",
            "ingredients": english_product.get("ingredients_text_en")
            or english_product.get("ingredients_text")
            or "N/A",
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/products")
def products():
    if "user_id" not in session:
        return redirect("/login")

    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT product_id, name, type, amazon_link, directions, shelf_life, ingredients
            FROM Products
            WHERE user_id=?
        """,
            (session["user_id"],),
        )
        product_list = cursor.fetchall()

    return render_template("/product/products.html", products=product_list)

@app.route("/reminders")
def reminders():
    return render_template("/reminder/reminders.html")

@app.route("/add_reminder", methods=["GET", "POST"])
def add_reminder():
    if request.method == "POST":
        reminder_type = request.form["reminder_type"]
        alarm_date = request.form["alarm_date"]
        recurrence = request.form["recurrence"]
        product_id = request.form.get("product_id") or None
        user_id = 1  # Replace with logged-in user in real app

        # # Save to DB (use SQLite or ORM)
        # conn = get_db_connection()
        # conn.execute(
        #     """
        #     INSERT INTO Reminders (reminder_type, alarm_date, recurrence, user_id, product_id)
        #     VALUES (?, ?, ?, ?, ?)
        # """,
        #     (reminder_type, alarm_date, recurrence, user_id, product_id),
        # )
        # conn.commit()
        # conn.close()

        return redirect(url_for("reminders"))

    # # For GET request – pull products for dropdown
    # conn = get_db_connection()
    # products = conn.execute("SELECT product_id, product_name FROM Products").fetchall()
    # conn.close()
    return render_template("add_reminder.html", products=products)


@app.route("/my_collection")
def my_collection():
    return render_template("collection/my_collection.html")

@app.route("/all_reviews")
def all_reviews():
    return render_template("review/all_reviews.html")



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
