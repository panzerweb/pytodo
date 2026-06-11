from pytodo.data.statistics_services import get_task_statistics
from pytodo.models.statistics_entity import StatisticsEntity

def progress_bar(percent: int, width: int = 20) -> str:
    filled = int(width * percent / 100)
    return "█" * filled + "░" * (width - filled)


def get_message(rate: int) -> str:
    if rate >= 90:
        return "🔥 Outstanding productivity!"
    elif rate >= 75:
        return "🚀 Great work!"
    elif rate >= 50:
        return "💪 Keep the momentum going!"
    else:
        return "🌱 Every completed task counts!"


def getStatistics() -> None:
    stats: StatisticsEntity = get_task_statistics()

    bar = progress_bar(stats.completion_rate)

    print("\n=================================")
    print("          PYTODO STATS")
    print("=================================\n")

    print(f"Today             : {stats.tasks_today_count}")
    print(f"Yesterday         : {stats.task_yesterday_count}")
    print()
    print(f"Total Tasks       : {stats.total_tasks_count}")
    print()
    print(f"✓ Completed       : {stats.complete_tasks_count}")
    print(f"✗ Incomplete      : {stats.incomplete_tasks_count}")
    print()
    print(f"Completion Rate   : {stats.completion_rate}%")
    print(f"[{bar}]")
    print()
    print(get_message(stats.completion_rate))
    print()
    print("=================================")