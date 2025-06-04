from flask import Blueprint, render_template, request, redirect, url_for, session, abort
import os
import requests
from datetime import datetime, timedelta
from flask import jsonify
from werkzeug.utils import secure_filename
from routes.product_ai import generate_product_description
import database.db_connector as db

product_bp = Blueprint(
    "product", __name__, url_prefix="", template_folder="../templates/product"
)


@product_bp.route("/all_products", methods=["GET"])
@product_bp.route("/all", methods=["GET"])
def view_all_product():
    if "user_id" not in session:
        return redirect("/user/login")

    user_id = session["user_id"]
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    products_query = "SELECT product_id AS id, product_name, amazon_link, ingredients, product_pic FROM Products ORDER BY product_id"
    cursor = db.execute_query(conn, query=products_query, query_params=())
    products = cursor.fetchall()

    collection_query = "SELECT product_id FROM Collections WHERE user_id = %s"
    cursor = db.execute_query(conn, query=collection_query, query_params=(user_id,))
    in_collection = cursor.fetchall()
    in_collection_ids = {row["product_id"] for row in in_collection}

    conn.close()
    return render_template(
        "product/all_products.html",
        products_list=products,
        in_collection_ids=in_collection_ids,
    )


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
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    product_data = {}

    if request.method == "POST":
        name = request.form.get("name")
        product_type = request.form.get("type")
        amazon_link = request.form.get("amazon_link")
        directions = request.form.get("directions")
        shelf_life = int(request.form.get("shelf_life"))
        ingredients = request.form.get("ingredients")
        pic_file = request.files.get("product_pic")
        filename = None

        if pic_file and pic_file.filename:
            filename = secure_filename(pic_file.filename)
            save_path = os.path.join("static", "images", filename)
            pic_file.save(save_path)

        if product_id:
            #  Update existing product
            if filename:
                query = "UPDATE Products SET product_name = %s, type = %s, amazon_link = %s, directions = %s, shelflife = %s, ingredients = %s, product_pic = %s WHERE product_id = %s"
                query_params = (
                    name,
                    product_type,
                    amazon_link,
                    directions,
                    shelf_life,
                    ingredients,
                    filename,
                    product_id,
                )

            else:
                query = "UPDATE Products SET product_name = %s, type = %s, amazon_link = %s, directions = %s, shelflife = %s, ingredients = %s WHERE product_id = %s"
                query_params = (
                    name,
                    product_type,
                    amazon_link,
                    directions,
                    shelf_life,
                    ingredients,
                    product_id,
                )
            cursor = db.execute_query(conn, query=query, query_params=query_params)
        else:
            # Add new product
            query = "INSERT INTO Products(user_id, product_name, type, amazon_link, directions, shelflife, ingredients, product_pic) VALUES ( % s, % s, % s, % s, % s, % s, % s, % s)"
            query_params = (
                session["user_id"],
                name,
                product_type,
                amazon_link,
                directions,
                shelf_life,
                ingredients,
                filename,
            )
            cursor = db.execute_query(conn, query=query, query_params=query_params)
            new_product_id = cursor.lastrowid

            # Add to collection
            db.execute_query(
                conn,
                "INSERT INTO Collections (user_id, product_id) VALUES (%s, %s)",
                (
                    session["user_id"],
                    new_product_id,
                ),
            )

            # Add expiration into reminders
            alarm_date = datetime.now() + timedelta(days=int(shelf_life))
            db.execute_query(
                conn,
                'INSERT INTO Reminders (reminder_type, alarm_date, recurrence, user_id, product_id) VALUES ("product shelf life / expiration", %s, %s, %s, %s)',
                (
                    alarm_date,
                    shelf_life,
                    session["user_id"],
                    new_product_id,
                ),
            )

        conn.close()
        return redirect(url_for("collection.my_collection"))

    # If editing, pre-fill form
    if product_id:
        query = "SELECT product_name, type, amazon_link, directions, shelflife, ingredients FROM Products WHERE product_id=%s"
        cursor = db.execute_query(conn, query=query, query_params=(product_id,))
        row = cursor.fetchone()

        if row:
            product_data = {
                "name": row["product_name"],
                "type": row["type"],
                "amazon_link": row["amazon_link"],
                "directions": row["directions"],
                "shelf_life": row["shelflife"],
                "ingredients": row["ingredients"],
            }

    conn.close()
    return render_template(
        "product/add_product.html", product=product_data, editing_id=product_id
    )


@product_bp.route("/delete_product/<int:id>", methods=["POST"])
def delete_product(id):
    if "user_id" not in session:
        return redirect("/user/login")

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    # Delete from Collections first
    db.execute_query(
        conn,
        "DELETE FROM Collections WHERE user_id=%s AND product_id=%s",
        (
            session["user_id"],
            id,
        ),
    )

    # Then delete the actual product
    db.execute_query(
        conn,
        "DELETE FROM Products WHERE product_id=%s AND user_id=%s",
        (
            id,
            session["user_id"],
        ),
    )

    conn.close()

    return redirect(url_for("collection.my_collection"))


@product_bp.route("/product/<int:product_id>", methods=["GET"])
def view_product(product_id):
    if "user_id" not in session:
        return redirect("/user/login")

    user_id = session["user_id"]
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    # Get product info
    query = "SELECT product_id, product_name, type, amazon_link, directions, shelflife, ingredients, product_pic FROM Products WHERE product_id = %s"
    cursor = db.execute_query(conn, query=query, query_params=(product_id,))
    product = cursor.fetchone()

    product = dict(product)
    directions = generate_product_description(product["product_name"])
    product["directions"] = directions

    if product is None:
        conn.close()
        abort(404)

    # Get product reviews
    cursor = db.execute_query(
        conn,
        query="SELECT review_note, review_photo FROM Reviews WHERE product_id= % s",
        query_params=(product_id,),
    )
    reviews = cursor.fetchall()

    # Get shared diary entries
    query = "SELECT diary_note, diary_photo FROM Diaries WHERE product_id = %s AND shared = 1"
    cursor = db.execute_query(conn, query=query, query_params=(product_id,))
    shared_diaries = cursor.fetchall()

    # Check if user already submitted review for product
    query = "SELECT 1 FROM Reviews WHERE user_id = %s AND product_id = %s LIMIT 1"
    cursor = db.execute_query(
        conn,
        query=query,
        query_params=(
            user_id,
            product_id,
        ),
    )

    user_has_reviewed = cursor.fetchone() is not None

    conn.close()

    ref = request.referrer or ""
    if "collection" in ref:
        back_url = url_for("collection.my_collection")
    else:
        back_url = url_for("product.view_all_product")

    return render_template(
        "product/product_info.html",
        product=product,
        product_reviews=reviews,
        shared_diaries=shared_diaries,
        user_has_reviewed=user_has_reviewed,
        back_url=back_url,
    )


@product_bp.route("/add_to_collection/<int:product_id>", methods=["POST"])
def add_to_collection(product_id):
    if "user_id" not in session:
        return redirect("/user/login")

    user_id = session["user_id"]
    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    cursor = db.execute_query(
        conn,
        query="SELECT 1 FROM Collections WHERE user_id=%s AND product_id=%s",
        query_params=(
            user_id,
            product_id,
        ),
    )
    exists = cursor.fetchone()

    if not exists:
        cursor = db.execute_query(
            conn,
            query="INSERT INTO Collections (user_id, product_id) VALUES (%s, %s)",
            query_params=(user_id, product_id),
        )

    conn.close()
    return redirect(url_for("product.view_all_product"))
