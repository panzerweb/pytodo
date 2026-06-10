from pytodo.models.task_entity import TaskEntity, TaskCreateDTO, TaskUpdateDTO
from typing import List
from datetime import date
import sqlite3

DATABASE_NAME: str = 'pytodo.db'

# Create module
def create(task: TaskCreateDTO) -> bool:
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

# Bulk Create of Tasks
def bulkCreate(tasks: List[TaskCreateDTO]):
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            bulk_add_query = """
            INSERT INTO tasks (name, description, category, status)
            VALUES (?,?,?,?)
            """

            parsedTasks = [tuple(task.__dict__.values()) for task in tasks]

            cursor.executemany(bulk_add_query, parsedTasks)

            connection.commit()
            
            return True
    except sqlite3.Error as e:
        print(f"Tasks creation error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Reading of tasks with optional parameters
def read(dateParams = None) -> List[TaskEntity]:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            parseDate: date = dateParams

            print(f"Passed date: {parseDate}")

            select_query = "SELECT * FROM tasks WHERE created_at = ? ORDER BY created_at DESC" if parseDate is not None else "SELECT * FROM tasks ORDER BY created_at DESC;"

            cursor.execute(select_query, (parseDate,) if parseDate is not None else ())

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
    
# Update of tasks today
def updateTaskToday(status: str, dateParams = None) -> str:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            parseDate: date = dateParams

            update_query = """
            UPDATE tasks SET status = ? WHERE created_at = ?
            """

            cursor.execute(update_query, (status, parseDate))

            if cursor.rowcount > 0:
                return "Tasks today updated successfully"
            else:
                return "No tasks today found"
    
    except sqlite3.Error as e:
        print(f"Failed to update tasks for today: {e}")
        return "Failed to update tasks for today"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Unexpected error"

# Update a task
def update(taskId: int, task: TaskUpdateDTO) -> str:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            fields = []
            values = []

            if task.name is not None:
                fields.append("name = ?")
                values.append(task.name)

            if task.description is not None:
                fields.append("description = ?")
                values.append(task.description)

            if task.category is not None:
                fields.append("category = ?")
                values.append(task.category)

            if task.status is not None:
                fields.append("status = ?")
                values.append(task.status)

            if not fields or len(fields) == 0:
                return False  # nothing to update

            values.append(taskId)

            update_query = f"""
            UPDATE tasks
            SET {', '.join(fields)}
            WHERE id = ?;
            """
            
            cursor.execute(update_query, values)

            connection.commit()

            # return cursor.rowcount > 0
            if cursor.rowcount > 0:
                return "Successfully updated task"
            else:
                return "No task found to update"
            

    except sqlite3.Error as e:
        print(f"Updating of tasks failed {e}")
        return "Updating of tasks failed"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Unexpected error"

# Delete a task
def delete(taskId: int) -> bool:
    try:
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            delete_query = """
            DELETE FROM tasks
            WHERE id = ?;
            """

            cursor.execute(delete_query, (taskId,))

            connection.commit()

            return True
    except sqlite3.Error as e:
        print(f"Error deleting task: {e}")
        return False
    except Exception as e:
        print(f"Something unexpected happen {e}")
        return False