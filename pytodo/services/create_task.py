from pytodo.models.list import List
from pytodo.services.json_services import load_json
from pytodo.services.json_services import save_list
from pytodo.services.json_services import save_backup
import json
import os
import uuid

# Locate pathfile using OS
BASE_DIR: str = os.path.dirname(__file__)  # directory of create.py
TASK_FILE: str = os.path.join(BASE_DIR, '..', 'tasks.json')
TASK_FILE: str = os.path.abspath(TASK_FILE)

BACKUP_FILE: str = os.path.join(BASE_DIR, '..', 'backup.json')
BACKUP_FILE: str = os.path.abspath(BACKUP_FILE)

def create_list(todos: str, description: str, created_at: str) -> None | List:
    tasks: list = load_json(TASK_FILE)

    if todos == '' or description == '':
        print("Please fill all the fields required")
        return

    # Creates an AUTO_INCREMENTING Id
    # Avoids duplicates by analyzing the maximum id
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    # Generates UUID
    new_uuid: str = str(uuid.uuid4())

    # Logic to add list
    new_list: List = List(new_id, new_uuid, todos, description, created_at)
    
    if new_list:
        tasks.append(new_list.to_dict())
        # Backup before saving
        save_backup(tasks, BACKUP_FILE)
        # Save to main file
        save_list(tasks, TASK_FILE)
        
        new_list.display_list()
        return new_list
    else:
        print("Creating new task failed")
        return