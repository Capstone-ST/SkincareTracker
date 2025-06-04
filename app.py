import sqlite3
import requests
from flask import Flask, session, jsonify
from routes.home_routes import home_bp
from routes.diary_routes import diary_bp
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.review_routes import review_bp
from routes.collection_routes import collection_bp
from routes.reminder_routes import reminder_bp

import database.db_connector as db


import os


st_db = "./database/skincare.db"  # short for skintracker database

app = Flask(__name__)

# Config
app.secret_key = os.environ.get(
    "SECRET_KEY", "supersecretkey"
)  # Use env var in production
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["SESSION_TYPE"] = "filesystem"

# Register Blueprints
app.register_blueprint(diary_bp, url_prefix="/diary")
app.register_blueprint(reminder_bp, url_prefix="/reminder")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(product_bp)
app.register_blueprint(review_bp, url_prefix="/review")
app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(collection_bp)


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


# DB helper
def get_db_connection():
    # conn = sqlite3.connect(st_db)
    # conn.row_factory = sqlite3.Row
    # return conn

    return db.connect_to_database()


# Make get_db_connection globally available
app.get_db_connection = get_db_connection

if __name__ == "__main__":
    app.run(debug=True)
