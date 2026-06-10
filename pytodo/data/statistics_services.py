import sqlite3
from datetime import datetime, timedelta
from pytodo.data.app_services import DATABASE_NAME
from pytodo.models.statistics_entity import StatisticsEntity

def get_task_statistics() -> StatisticsEntity:
    try:
        today = datetime.now()
        yesterday = (datetime.now() - timedelta(days=1))

        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()

            tasks_count_for_today_query = "SELECT COUNT(*) FROM tasks WHERE created_at = ?"
            tasks_count_for_yesterday_query = "SELECT COUNT(*) FROM tasks WHERE created_at = ?"
            completed_tasks_count_query = "SELECT COUNT(*) FROM tasks WHERE status = 'complete'"
            incomplete_tasks_count_query = "SELECT COUNT(*) FROM tasks WHERE status != 'complete'"

            cursor.execute(tasks_count_for_today_query, (today,))
            today_count = cursor.fetchone()[0]

            cursor.execute(tasks_count_for_yesterday_query, (yesterday,))
            yesterday_count = cursor.fetchone()[0]

            cursor.execute(completed_tasks_count_query)
            completed_tasks_count = cursor.fetchone()[0]

            cursor.execute(incomplete_tasks_count_query)
            incomplete_tasks_count = cursor.fetchone()[0]

        return StatisticsEntity(tasks_today_count=today_count, 
                                task_yesterday_count=yesterday_count, 
                                complete_tasks_count=completed_tasks_count, 
                                incomplete_tasks_count=incomplete_tasks_count
                                )
    except sqlite3.Error as e:
        print(f"Error fetching statistics: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None



            