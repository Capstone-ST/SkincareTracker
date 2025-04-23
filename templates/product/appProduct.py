import os
import sqlite3
from flask import jsonify
import requests
from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

import database.create_db

st_db = "skincare.db"                    # short for skintracker database
# db_connection = database.create_db()







