import os
import sqlite3
from flask import jsonify
import requests
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret_key"
UPLOAD_FOLDER = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Simulated INCIdecoder ingredient database
ingredient_database = {
    "niacinamide": {
        "type": "Serum",
        "amazon_link": "https://www.amazon.com/dp/B079DFPZPJ",
        "directions": "Apply morning and night",
        "shelf_life": "12",
        "ingredients": "Niacinamide, Zinc PCA, Water"
    },
    "salicylic acid": {
        "type": "Cleanser",
        "amazon_link": "https://www.amazon.com/dp/B00LW2GM84",
        "directions": "Use in evening",
        "shelf_life": "9",
        "ingredients": "Salicylic Acid, Glycerin, Water"
    }
}

#  DB Initialization
def init_db():
    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                email TEXT,
                age INTEGER,
                skintype TEXT,
                picture TEXT DEFAULT 'default.png'
            )
        ''')
        # Products table
        cursor.execute('''
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
        ''')
        conn.commit()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Users WHERE username=? AND password=?', (username, password))
            user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]
            return redirect('/homepage')
        error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        age = request.form['age']
        skintype = request.form['skintype']

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO Users (username, password, email, age, skintype)
                    VALUES (?, ?, ?, ?, ?)
                ''', (username, password, email, age, skintype))
                conn.commit()
                return redirect('/login')
            except sqlite3.IntegrityError:
                error = "Username already exists."

    return render_template('register.html', error=error)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/login')
    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, email, age, skintype, picture FROM Users WHERE user_id=?', (session['user_id'],))
        user = cursor.fetchone()
    return render_template('profile.html', user={
        'username': user[0],
        'email': user[1],
        'age': user[2],
        'skintype': user[3],
        'picture': user[4]
    })

@app.route('/upload-profile-picture', methods=['POST'])
def upload_profile_picture():
    if 'user_id' not in session:
        return redirect('/login')
    file = request.files.get('profile_picture')
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Users SET picture=? WHERE user_id=?', (filename, session['user_id']))
            conn.commit()
    return redirect('/profile')


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        email = request.form.get('email')
        age = request.form.get('age')
        skintype = request.form.get('skintype')

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Users SET email=?, age=?, skintype=?
                WHERE user_id=?
            ''', (email, age, skintype, session['user_id']))
            conn.commit()
        return redirect('/profile')

    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        #  Add picture here
        cursor.execute('SELECT email, age, skintype, picture FROM Users WHERE user_id=?', (session['user_id'],))
        data = cursor.fetchone()

    return render_template('edit_profile.html', user={
        'email': data[0],
        'age': data[1],
        'skintype': data[2],
        'picture': data[3]
    })


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if 'user_id' not in session:
        return redirect('/login')

    product_id = request.args.get('id')

    if request.method == 'POST':
        name = request.form.get('name')
        product_type = request.form.get('type')
        amazon_link = request.form.get('amazon_link')
        directions = request.form.get('directions')
        shelf_life = request.form.get('shelf_life')
        ingredients = request.form.get('ingredients')

        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            if product_id:
                cursor.execute('''
                    UPDATE Products SET name=?, type=?, amazon_link=?, directions=?, shelf_life=?, ingredients=?
                    WHERE product_id=? AND user_id=?
                ''', (name, product_type, amazon_link, directions, shelf_life, ingredients, product_id, session['user_id']))
            else:
                cursor.execute('''
                    INSERT INTO Products (user_id, name, type, amazon_link, directions, shelf_life, ingredients)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (session['user_id'], name, product_type, amazon_link, directions, shelf_life, ingredients))
            conn.commit()
        return redirect('/products')

    product_data = {}
    if product_id:
        with sqlite3.connect("skincare.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT name, type, amazon_link, directions, shelf_life, ingredients 
                FROM Products 
                WHERE product_id=? AND user_id=?
            ''', (product_id, session['user_id']))
            row = cursor.fetchone()
            if row:
                product_data = {
                    'name': row[0],
                    'type': row[1],
                    'amazon_link': row[2],
                    'directions': row[3],
                    'shelf_life': row[4],
                    'ingredients': row[5]
                }

    return render_template('add_product.html', product=product_data, editing_id=product_id)

@app.route('/delete-product/<int:id>', methods=['POST'])
def delete_product(id):
    if 'user_id' not in session:
        return redirect('/login')

    try:
        with sqlite3.connect("skincare.db", isolation_level=None) as conn:
            cursor = conn.cursor()
            cursor.execute('PRAGMA busy_timeout = 5000')
            cursor.execute('DELETE FROM Products WHERE product_id=? AND user_id=?', (id, session['user_id']))
    except sqlite3.OperationalError as e:
        return f"Database error: {e}", 500

    return redirect('/products')

@app.route('/api/featured-products')
def featured_products():
    response = requests.get('https://world.openbeautyfacts.org/cgi/search.pl', params={
        'search_terms': 'skincare',
        'search_simple': 1,
        'action': 'process',
        'json': 1,
        'page_size': 20
    })
    data = response.json()
    products = []

    for product in data.get('products', []):
        name = product.get('product_name_en') or product.get('product_name')
        ingredients = product.get('ingredients_text_en') or product.get('ingredients_text')
        image = product.get('image_front_url', '')

        if name and ingredients and image:
            products.append({
                'name': name,
                'image': image,
                'ingredients': ingredients
            })

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


@app.route('/api/get-product-info', methods=['POST'])
def get_product_info():
    product_name = request.form.get('name')
    if not product_name:
        return jsonify({'error': 'Missing product name'}), 400

    try:
        response = requests.get(
            'https://world.openbeautyfacts.org/cgi/search.pl',
            params={
                'search_terms': product_name,
                'search_simple': 1,
                'action': 'process',
                'json': 1,
                'lc': 'en',
                'page_size': 10
            }
        )
        data = response.json()
        products = data.get("products", [])

        english_product = None
        for p in products:
            if (
                p.get("ingredients_text_en") or
                p.get("product_name_en") or
                p.get("lang") == "en"
            ):
                english_product = p
                break

        if not english_product:
            return jsonify({'error': 'No English product found'}), 404

        result = {
            "type": extract_type_from_categories(english_product.get("categories", "")),
            "amazon_link": "#",
            "directions": "N/A",
            "shelf_life": "6",
            "ingredients": english_product.get("ingredients_text_en") or english_product.get("ingredients_text") or "N/A"
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/products')
def products():
    if 'user_id' not in session:
        return redirect('/login')

    with sqlite3.connect("skincare.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT product_id, name, type, amazon_link, directions, shelf_life, ingredients
            FROM Products
            WHERE user_id=?
        ''', (session['user_id'],))
        product_list = cursor.fetchall()

    return render_template('products.html', products=product_list)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)






