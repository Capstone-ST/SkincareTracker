from flask import Blueprint, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

product_bp = Blueprint("product", __name__, template_folder="../templates/product")


@product_bp.route("/all_products")
def view_all_product():
    user_id = session.get("user_id", 1)
    # conn = product_bp.root_path.split("/routes")[0]
    db = __import__("app").app.get_db_connection()
    products = db.execute(
        """
        SELECT *
        FROM Products
        ORDER BY Products.product_id
        """,
    ).fetchall()
    print(products)
    db.close()
    return render_template("product/all_products.html", products_list=products)


@product_bp.route("/add", methods=["GET", "POST"])
def add_product():
    user_id = session.get("user_id", 1)

    if request.method == "POST":
        date = request.form["date"]
        product_id = request.form.get("product_id") or None
        body_part = request.form["body_part"]
        acne = 1 if "acne" in request.form else 0
        adverse = 1 if "adverse" in request.form else 0
        product_note = request.form["product_note"]

        # Insert into DB
        db = __import__("app").app.get_db_connection()
        entries = db.execute(
            """
            INSERT INTO Diaries (user_id, date, product_id, body_part, acne, adverse, product_note, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                user_id,
                date,
                product_id,
                body_part,
                acne,
                adverse,
                product_note,
            ),
        )
        db.commit()
        db.close()

        return redirect(url_for("product"))

    return render_template("add_product.html")
