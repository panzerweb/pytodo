from pytodo.models.list import List
from pytodo.services.fetch import load_json
from pytodo.services.fetch import save_list
import json
import os
import uuid

# Locate pathfile using OS
BASE_DIR = os.path.dirname(__file__)  # directory of create.py
TASK_FILE = os.path.join(BASE_DIR, '..', 'tasks.json')
TASK_FILE = os.path.abspath(TASK_FILE)

def create_list(todos, description, created_at):
    tasks = load_json(TASK_FILE)

    # Creates an AUTO_INCREMENTING Id
    # Avoids duplicates by analyzing the maximum id
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1

    # Generates UUID
    new_uuid = str(uuid.uuid4())

    # Logic to add list
    new_list = List(new_id, new_uuid, todos, description, created_at)
    tasks.append(new_list.to_dict())
    save_list(tasks, TASK_FILE)
    
    new_list.display_list()
    return new_list