# import os
# import sqlite3

# def connect_to_database(database):
#     """
#     connects to a database and returns a database objects
#     """
#     db_connection = sqlite3.connect(database)
#     db_connection.row_factory = sqlite3.Row
#     return db_connection


import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

# Load our environment variables from the .env file in the root of our project.
load_dotenv(find_dotenv())

# Set the variables in our application with those environment variables
host = os.environ.get("467DBHOST")
user = os.environ.get("467DBUSER")
passwd = os.environ.get("467DBPW")
db = os.environ.get("467DB")


def connect_to_database(host=host, user=user, passwd=passwd, db=db):
    """
    connects to a database and returns a database objects
    """
    db_connection = MySQLdb.connect(host, user, passwd, db)
    return db_connection


def execute_query(db_connection=connect_to_database(), query=None, query_params=()):
# def execute_query(query=None, query_params=()):
    """
    executes a given SQL query on the given db connection and returns a Cursor object

    db_connection: a MySQLdb connection object created by connect_to_database()
    query: string containing SQL query

    returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
    You need to run .fetchall() or .fetchone() on that object to actually acccess the results.

    """


    if db_connection is None:
        print(
            "No connection to the database found! Have you called connect_to_database() first?"
        )
        return None

    if query is None or len(query.strip()) == 0:
        print("query is empty! Please pass a SQL query in query")
        return None

    print("Executing %s with %s" % (query, query_params))
    # Create a cursor to execute query. Why? Because apparently they optimize execution by retaining a reference according to PEP0249
    cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute(query, query_params)

    db_connection.commit()
    return cursor


if __name__ == "__main__":
    print(
        "Executing a sample query on the database using the credentials from db_credentials.py"
    )
    db = connect_to_database()
    query = "SELECT * from Products;"
    results = execute_query(db, query)
    print("Printing results of %s" % query)

    for r in results.fetchall():
        print(r)
