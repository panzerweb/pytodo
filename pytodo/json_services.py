import json
import os

# This file will handle the saving and loading of data from
# external files such as .json

# PRODUCTION-BASE FUNCTION FOR CREATING A FOLDER WHEN DEPLOYED
# Stores data on tasks.json in production
# STORE TASK
def get_data_file():
    appdata = os.getenv("APPDATA")
    app_folder = os.path.join(appdata, "PyTodo")

    if not os.path.exists(app_folder):
        os.makedirs(app_folder)
    
    return os.path.join(app_folder, "tasks.json")

DATA_FILE = get_data_file()

# Loads tasks from the production folder
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
        
    return []

# Saves tasks on the production folder
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

#============================================================

# DEVELOPMENT ENVIRONMENT
# Loads the JSON file
def load_json(file_path) -> list:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # If file is empty or corrupted, start fresh
                return []
    return []

# Save the data to the JSON.file
def save_list(tasks, file_path) -> None:
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

# Save the data to the backup JSON.file
def save_backup(tasks, file_path) -> None:
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)
