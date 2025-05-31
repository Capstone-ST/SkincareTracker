from flask import Blueprint, render_template, session, redirect

collection_bp = Blueprint("collection", __name__, url_prefix="/collection", template_folder="../templates/collection")

@collection_bp.route("/", methods=["GET"])
def my_collection():
    if "user_id" not in session:
        return redirect("/user/login")

    db = __import__("app").app.get_db_connection()
    products = db.execute(
        """
        SELECT P.product_id, P.product_name, P.type, P.amazon_link, P.directions, P.shelflife, P.ingredients, P.product_pic
        FROM Products P
        JOIN Collections C ON P.product_id = C.product_id
        WHERE C.user_id = ?
        """,
        (session["user_id"],)
    ).fetchall()

    db.close()
    return render_template("collection/my_collection.html", products=products)
