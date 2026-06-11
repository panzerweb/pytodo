import sqlite3
import os

APP_DIR = os.path.join(os.getenv("APPDATA"), "PyTodo")
os.makedirs(APP_DIR, exist_ok=True)

DB_PATH = os.path.join(APP_DIR, "pytodo.db")

def activateDb():
    try:
        with sqlite3.connect(DB_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            # Let's create the table tasks
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL DEFAULT '',
                description TEXT NOT NULL DEFAULT '',
                category TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'incomplete',
                CHECK (status IN ('complete', 'incomplete')),
                created_at DATE NOT NULL DEFAULT CURRENT_DATE
            );
            '''

            # Only use this to alter a table and comment other query
            # alter_query = '''
            # ALTER TABLE tasks 
            # ADD COLUMN created_at DATE NOT NULL DEFAULT CURRENT_DATE;
            # '''

            create_index_query = '''
            CREATE INDEX IF NOT EXISTS idx_task_status 
            ON tasks(status);
            '''

            cursor.execute(create_table_query)
            # cursor.execute(alter_query)
            cursor.execute(create_index_query)

            connection.commit()

    except sqlite3.Error as e:
    # Fix 3: Catch specific errors and print the message for debugging
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")