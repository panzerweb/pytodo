from datetime import date
from dataclasses import dataclass, asdict

@dataclass
class TaskEntity:
    name: str | None = None
    category: str | None = None
    created_at: date = date.today()
    description: str | None = None
    status: str = "incomplete"
    id: int | None = None

    def to_dict(self):
        return asdict(self)
    
class TaskUpdateDTO:
    def __init__(self,
        name: str | None = None,
        description: str | None = None,
        category: str | None = None,
        status: str | None = None,
    ):
        self.name = name
        self.description = description
        self.category = category
        self.status = status
        