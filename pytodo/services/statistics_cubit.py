from pytodo.data.statistics_services import get_task_statistics
from pytodo.models.statistics_entity import StatisticsEntity

def getStatsCount():
    stats: StatisticsEntity = get_task_statistics()

    print(f"Today: {stats.tasks_today_count}, Yesterday: {stats.task_yesterday_count}")
    print(f"Completed: {stats.complete_tasks_count}, Incomplete: {stats.incomplete_tasks_count}")