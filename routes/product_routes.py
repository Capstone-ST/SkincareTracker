from flask import Blueprint, render_template, request, redirect, url_for, session
import os
import requests
from datetime import datetime, timedelta
from flask import jsonify
from werkzeug.utils import secure_filename
from routes.product_ai import generate_product_description

product_bp = Blueprint("product", __name__, url_prefix="", template_folder="../templates/product")

@product_bp.route("/all_products", methods=["GET"])
@product_bp.route("/all", methods=["GET"])
def view_all_product():
    if "user_id" not in session:
        return redirect("/user/login")

    db = __import__("app").app.get_db_connection()

    # Show all products from all users
    products = db.execute("""
        SELECT
          product_id AS id,
          product_name,
          amazon_link,
          ingredients
        FROM Products
        ORDER BY product_id
    """).fetchall()

    db.close()
    return render_template("product/all_products.html", products_list=products)

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

@product_bp.route("/api/get-product-info", methods=["POST"])
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


@product_bp.route("/add_product", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session:
        return redirect("/user/login")

    product_id = request.form.get("product_id") or request.args.get("id")
    db = __import__("app").app.get_db_connection()
    product_data = {}

    if request.method == "POST":
        name = request.form.get("name")
        product_type = request.form.get("type")
        amazon_link = request.form.get("amazon_link")
        directions = request.form.get("directions")
        shelf_life = request.form.get("shelf_life")
        ingredients = request.form.get("ingredients")

        if product_id:
            #  Update existing product
            db.execute(
                """
                UPDATE Products
                SET product_name=?, type=?, amazon_link=?, directions=?, shelflife=?, ingredients=?
                WHERE product_id=?
                """,
                (
                    name, product_type, amazon_link,
                    directions, shelf_life, ingredients, product_id
                )
            )
        else:
            #  Add new product
            cursor = db.execute(
                """
                INSERT INTO Products (user_id, product_name, type, amazon_link, directions, shelflife, ingredients)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    session["user_id"], name, product_type,
                    amazon_link, directions, shelf_life, ingredients
                )
            )
            new_product_id = cursor.lastrowid

            #  Add to collection
            db.execute(
                "INSERT INTO Collections (user_id, product_id) VALUES (?, ?)",
                (session["user_id"], new_product_id)
            )

            # Add expiration into reminders
            alarm_date = datetime.now() + timedelta(shelf_life)
            db.execute(
                """INSERT INTO Reminders (reminder_type, alarm_date, recurrence, user_id, product_id)
               VALUES ("product shelf life / expiration", ?, ?, ?, ?)""",
                (
                    alarm_date,
                    shelf_life,
                    session["user_id"],
                    product_id,
                ),
            )

        db.commit()
        db.close()
        return redirect(url_for("collection.my_collection"))

    # If editing, pre-fill form
    if product_id:
        row = db.execute(
            "SELECT product_name, type, amazon_link, directions, shelflife, ingredients FROM Products WHERE product_id=?",
            (product_id,)
        ).fetchone()

        if row:
            product_data = {
                "name": row[0],
                "type": row[1],
                "amazon_link": row[2],
                "directions": row[3],
                "shelf_life": row[4],
                "ingredients": row[5],
            }

    db.close()
    return render_template("product/add_product.html", product=product_data, editing_id=product_id)


@product_bp.route("/delete_product/<int:id>", methods=["POST"])
def delete_product(id):
    if "user_id" not in session:
        return redirect("/user/login")

    db = __import__("app").app.get_db_connection()

    # Delete from Collections first
    db.execute(
        """
        DELETE FROM Collections WHERE user_id=? AND product_id=?
        """,
        (session["user_id"], id)
    )

    # Then delete the actual product
    db.execute(
        """
        DELETE FROM Products WHERE product_id=? AND user_id=?
        """,
        (id, session["user_id"])
    )

    db.commit()
    db.close()

    return redirect(url_for("collection.my_collection"))

@product_bp.route("/product/<int:product_id>", methods=["GET"])
def view_product(product_id):
    if "user_id" not in session:
        return redirect("/user/login")

    user_id = session["user_id"]
    db = __import__("app").app.get_db_connection()

    # Get product info
    product = db.execute(
        """
        SELECT
          product_id,
          product_name,
          type,
          amazon_link,
          directions,
          shelflife,
          ingredients,
          product_pic
        FROM Products
        WHERE product_id = ?
        """,
        (product_id,)
    ).fetchone()
    
    product = dict(product) 
    directions = generate_product_description(product['product_name'])
    product['directions'] = directions

    if product is None:
        db.close()
        abort(404)

    # Get product reviews
    reviews = db.execute(
        """
        SELECT review_note, review_photo
        FROM Reviews
        WHERE product_id = ?
        """,
        (product_id,)
    ).fetchall()

    # Get shared diary entries
    shared_diaries = db.execute(
        """
        SELECT diary_note, diary_photo
        FROM Diaries
        WHERE product_id = ? AND shared = 1
        """,
        (product_id,)
    ).fetchall()

    # Check if user already submitted review for product
    user_has_reviewed = db.execute(
        """
        SELECT 1
        FROM Reviews
        WHERE user_id = ? AND product_id = ?
        LIMIT 1
        """,
        (user_id, product_id)
    ).fetchone() is not None

    db.close()

    return render_template(
        "product/product_info.html",
        product=product,
        product_reviews=reviews,
        shared_diaries=shared_diaries,
        user_has_reviewed=user_has_reviewed
    )

