import os
import sqlite3
from flask import jsonify
import requests
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

import database.conn_db

st_db = "./database/skincare.db"  # short for skintracker database
# db_connection = database.conn_db(st_db)



def login_user(session, error=None):
    # return render_template("/user/hompeage.html")
    username = request.form["username"]
    password = request.form["password"]
    with sqlite3.connect(st_db) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM Users WHERE username=? AND password=?",
            (username, password),
        )
        user = cursor.fetchone()
    
    if user:
        return user[0]
    

