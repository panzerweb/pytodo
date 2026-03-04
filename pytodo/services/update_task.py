from pathlib import Path
from pytodo.json_services import load_tasks
from pytodo.json_services import save_tasks
from colorama import init, Fore, Style

def update_task(tasks: list, task_id: int, new_todo: str, new_description: str) -> list:
    for task in tasks:
        if task['id'] == task_id:
            if new_todo:
                task['todo'] = new_todo
            if new_description:
                task['description'] = new_description
            # save_list(tasks, to_save_path)
            # save_backup(tasks, to_backup_path)
            print(Fore.GREEN + f"Task {task_id} data updated.")
            return tasks
    print(Fore.RED + f"No task found with ID {task_id}.")
    return tasks