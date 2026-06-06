from datetime import date

class TaskEntity:
     # Initializes data models for class task
    def __init__(self, name: str, description: str, category: str, created_at: date,status='incomplete', id: int | None = None):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "status": self.status,
            "created_at": self.created_at
        }
    
