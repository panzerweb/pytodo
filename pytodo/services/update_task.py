from pathlib import Path
from pytodo.services.json_services import load_json
from pytodo.services.json_services import save_list
from pytodo.services.json_services import save_backup
from colorama import init, Fore, Style

to_save_path = Path('../pytodo/pytodo/tasks.json')
to_backup_path = Path('../pytodo/pytodo/backup.json')

def update_task(task_id: int, new_todo: str, new_description: str) -> None:
    tasks = load_json(to_save_path)

    for task in tasks:
        if task['id'] == task_id:
            if new_todo:
                task['todo'] = new_todo
            if new_description:
                task['description'] = new_description
            save_list(tasks, to_save_path)
            save_backup(tasks, to_backup_path)
            print(Fore.GREEN + f"Task {task_id} data updated.")
            return tasks
    print(Fore.RED + f"No task found with ID {task_id}.")
    return None