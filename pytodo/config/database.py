import sqlite3
import os

APP_DIR = os.path.join(os.getenv("APPDATA"), "PyTodo")
os.makedirs(APP_DIR, exist_ok=True)

DB_PATH = os.path.join(APP_DIR, "pytodo.db")

def activateDb():
    try:
        # print(f"DB Path: {DB_PATH}")

        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL DEFAULT '',
                description TEXT NOT NULL DEFAULT '',
                category TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'incomplete',
                created_at DATE NOT NULL DEFAULT CURRENT_DATE,
                CHECK (status IN ('complete', 'incomplete'))
            );
            """)

            connection.commit()

            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table';
            """)

            # print("Tables:", cursor.fetchall())

            # print("Database initialized successfully.")

    except sqlite3.Error as e:
    # Fix 3: Catch specific errors and print the message for debugging
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")