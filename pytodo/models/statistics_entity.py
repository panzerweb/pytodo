from dataclasses import dataclass, asdict

@dataclass
class StatisticsEntity:
    tasks_today_count: int
    task_yesterday_count: int
    complete_tasks_count: int
    incomplete_tasks_count: int

    