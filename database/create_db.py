import sqlite3
import os


def create_db(db_filename="skincare.db", sql_filename="schema.sql"):
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build absolute paths relative to the script
    db_path = os.path.join(base_dir, db_filename)
    sql_path = os.path.join(base_dir, sql_filename)

    try:
        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect(db_path)

        # Open and read the SQL schema file
        with open(sql_path, "r", encoding="utf-8") as sql_file:
            sql_script = sql_file.read()

        # Execute the SQL script
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        print(f"Tables created successfully in '{db_filename}'")

    except sqlite3.Error as e:
        print("An SQLite error occurred:", e)
    except FileNotFoundError:
        print(f"SQL file not found at: {sql_path}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # create_db()
    create_db(db_filename="skincare.db", sql_filename="schema.sql")
