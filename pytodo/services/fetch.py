import json
import os

# Loads the JSON file
def load_json(file_path):
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
def save_list(tasks, file_path):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

# Save the data to the backup JSON.file
def save_backup(tasks, file_path):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)
