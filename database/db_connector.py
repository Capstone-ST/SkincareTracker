import os
import sqlite3

def connect_to_database(database):
    """
    connects to a database and returns a database objects
    """
    db_connection = sqlite3.connect(database)
    return db_connection
