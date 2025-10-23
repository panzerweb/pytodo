from pytodo.services.create import create_list
from pytodo.services.fetch import *
from pytodo.services.delete import delete_task
from pytodo.services.search import search_by_date
from datetime import date
from colorama import Fore, Style, init
import os

from pytodo.menu import *

init(autoreset=True)

# get the directory of the current script (main.py)
BASE_DIR = os.path.dirname(__file__)
TASK_FILE = os.path.join(BASE_DIR, 'tasks.json')

def main():

    # init
    clear_screen()
    show_title()
    show_menu()

    # Sets current date
    current_date = date.today()

    while True:
        chosen_input = input("\nYou: ").strip().lower()

        if chosen_input == 'quit':
            break
        
        # Add a task
        elif chosen_input == 'add':
            task_input = input("Task name: ")

            create_list(task_input, str(current_date))

        # View all tasks
        elif chosen_input == 'view':
            tasks = load_json(TASK_FILE)

            if not tasks:
                print(Fore.LIGHTBLACK_EX + "📭 No tasks yet.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS ═══════════════════════\n")

                today_tasks = [task for task in tasks if task["created_at"] == str(current_date)]

                if today_tasks:
                    for i, task in enumerate(today_tasks, start=1):
                        print(Fore.YELLOW + f"🗓  Task {i}")
                        print(Fore.WHITE + f"   • Task ID     : {task['id']}")
                        print(f"   • Description : {task['todo']}")
                        print(f"   • Created At  : {task['created_at']}")
                        print(Fore.CYAN + "────────────────────────────────────────────────────────────")
                    print(Fore.GREEN + Style.BRIGHT + f"\n✅ {len(today_tasks)} task(s) for today ({current_date})\n")
                else:
                    print(Fore.RED + "😴 No tasks for today.")
                    print(Fore.LIGHTBLACK_EX + f"   Date checked: {current_date}\n")

        # Search task by date (yyyy-mm-dd)
        elif chosen_input == 'search':
            tasks = load_json(TASK_FILE)

            date_input: str = input("Enter date (yyyy-mm-dd): ")

            search_by_date(date_input, tasks)

        # Delete a task by their id
        elif chosen_input == 'delete':
            tasks = load_json(TASK_FILE)

            id_input = input("Enter id: ")

            result = [task["id"] for task in tasks if task["id"] == int(id_input)]

            if result:
                delete_task(int(id_input), tasks)
                save_list(tasks, TASK_FILE)

                print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} deleted successfully ═══════════════\n")

            else:
                print(Fore.RED + f"No task found with that ID.")

        # Else
        else:
            print("⚠ Invalid command. Try 'add', 'view', 'search', 'delete' or 'quit'.")

if __name__ == '__main__':
    main()