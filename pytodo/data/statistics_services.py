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

            all_tasks_count = "SELECT COUNT(*) FROM tasks"
            tasks_count_for_today_query = "SELECT COUNT(*) FROM tasks WHERE created_at = ?"
            tasks_count_for_yesterday_query = "SELECT COUNT(*) FROM tasks WHERE created_at = ?"
            completed_tasks_count_query = "SELECT COUNT(*) FROM tasks WHERE status = 'complete'"
            incomplete_tasks_count_query = "SELECT COUNT(*) FROM tasks WHERE status != 'complete'"

            cursor.execute(all_tasks_count)
            total_tasks:int = cursor.fetchone()[0]

            cursor.execute(tasks_count_for_today_query, (today,))
            today_count: int = cursor.fetchone()[0]

            cursor.execute(tasks_count_for_yesterday_query, (yesterday,))
            yesterday_count: int = cursor.fetchone()[0]

            cursor.execute(completed_tasks_count_query)
            completed_tasks_count: int = cursor.fetchone()[0]

            cursor.execute(incomplete_tasks_count_query)
            incomplete_tasks_count: int = cursor.fetchone()[0]

            # Completion Rate
            # Formula: completion_rate = (completed / total_tasks) * 100
            completion_rate = (completed_tasks_count / total_tasks) * 100

        return StatisticsEntity(
                                total_tasks_count=total_tasks,
                                tasks_today_count=today_count, 
                                task_yesterday_count=yesterday_count, 
                                complete_tasks_count=completed_tasks_count, 
                                incomplete_tasks_count=incomplete_tasks_count,
                                completion_rate=completion_rate,
                                )
    except sqlite3.Error as e:
        print(f"Error fetching statistics: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None



            