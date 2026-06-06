from pytodo.models.task_entity import TaskEntity
from typing import List
import sqlite3

DATABASE_NAME: str = 'pytodo.db'

# Create module
def create(task: TaskEntity) -> bool:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            insert_query = '''
            INSERT INTO tasks (name, description, category, status)
            VALUES (?,?,?,?);
            '''

            data = (task.name, task.description, task.category, task.status)

            cursor.execute(insert_query, data)    

            task.id = cursor.lastrowid

            connection.commit()
            
            return True

    except sqlite3.Error as e:
        print(f"Task creation error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    
def read() -> List[TaskEntity]:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            select_query = "SELECT * FROM tasks"

            cursor.execute(select_query)

            rows = cursor.fetchall()

            all_tasks: List[TaskEntity] = []
            
            for row in rows:
                task = TaskEntity(id=row[0], name=row[1], description=row[2], category=row[3], status=row[4], created_at=row[5])
                all_tasks.append(task)

            return all_tasks
        
    except sqlite3.Error as e:
        print(f"Fetching of tasks failed {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    