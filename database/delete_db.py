import os
import sqlite3

def delete_db(database_file="skincare.db"):
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build absolute paths relative to the script
    db_path = os.path.join(base_dir, database_file)

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DROP TABLE IF EXISTS Reminders;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS Reviews;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS Diarys;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS Collections;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS Products;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS Users;
        """)
        conn.commit()
    if conn:
        conn.close()


if __name__ == "__main__":
    delete_db(database_file="skincare.db")
