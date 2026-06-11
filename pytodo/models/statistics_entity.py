from dataclasses import dataclass, asdict

@dataclass
class StatisticsEntity:
    total_tasks_count: int
    tasks_today_count: int
    task_yesterday_count: int
    complete_tasks_count: int
    incomplete_tasks_count: int
    completion_rate: int

    