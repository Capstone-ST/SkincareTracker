from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import database.db_connector as db

load_dotenv()
collection_bp = Blueprint(
    "collection",
    __name__,
    url_prefix="/collection",
    template_folder="../templates/collection",
)


@collection_bp.route("/collection", methods=["GET"])
@collection_bp.route("/", methods=["GET"])
def my_collection():
    if "user_id" not in session:
        return redirect("/user/login")

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT P.product_id, P.product_name, P.type, P.amazon_link, P.directions, P.shelflife, P.ingredients, P.product_pic FROM Products P JOIN Collections C ON P.product_id = C.product_id WHERE C.user_id = %s"
    cursor = db.execute_query(conn, query=query, query_params=(session["user_id"],))
    products = cursor.fetchall()
    conn.close()

    return render_template("collection/my_collection.html", products=products)


@collection_bp.route("/product_rec", methods=["POST"])
def product_rec():
    user_id = session.get("user_id", 1)

    conn = __import__("app").app.get_db_connection()
    cursor = conn.cursor()

    products_query = "SELECT P.product_id, P.product_name, P.type, P.amazon_link, P.directions, P.shelflife, P.ingredients, P.product_pic FROM Products P JOIN Collections C ON P.product_id = C.product_id WHERE C.user_id = %s"
    cursor = db.execute_query(
        conn, query=products_query, query_params=(session["user_id"],)
    )
    products = cursor.fetchall()

    entries_query = (
        "SELECT diary_note FROM Diaries WHERE user_id = %s ORDER BY date DESC"
    )
    cursor = db.execute_query(
        conn, query=entries_query, query_params=(session["user_id"],)
    )
    entries = cursor.fetchall()
    conn.close()

    combined_notes = (
        "The user has the following products:"
        + str(
            [product["product_name"] for product in products if product["product_name"]]
        )
        + " and here are some user feelings: "
        + str([entry["diary_note"] for entry in entries if entry["diary_note"]])
    )
    # combined_notes = " ".join(
    #     [entry["diary_note"] for entry in entries if entry["diary_note"]]
    # )

    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

        response = llm.invoke(
            [
                SystemMessage(content="You are a knowledgeable skincare assistant."),
                HumanMessage(
                    content=f"Look at what the user has in their skincare collection and recommend three products:\n\n{combined_notes}"
                ),
            ]
        )

        flash(response.content, "info")

    except Exception as e:
        flash(f"AI summary failed: {str(e)}", "danger")

    return redirect(url_for("collection.my_collection") + "#product_rec")
