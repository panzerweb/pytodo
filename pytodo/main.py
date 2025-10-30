from pytodo.services.create import create_list
from pytodo.services.fetch import *
from pytodo.services.delete import delete_task
from pytodo.services.search import search_by_date
from pytodo.services.load import *
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
            desc_input = input("Description: ")

            # Execute function
            create_list(task_input, desc_input, str(current_date))

        # View all tasks for today
        elif chosen_input == 'view':
            tasks = load_json(TASK_FILE)

            if not tasks:
                print(Fore.LIGHTBLACK_EX + "📭 No tasks yet.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS FOR TODAY ═══════════════════════\n")

                # Calls the function
                view_task_today(tasks, current_date)

        # View all tasks
        elif chosen_input == 'view_all':
            tasks = load_json(TASK_FILE)

            if not tasks:
                print(Fore.LIGHTBLACK_EX + "📭 You have no tasks at all.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS ═══════════════════════\n")

                # Calls the function
                view_all(tasks)

        # Search task by date (yyyy-mm-dd)
        elif chosen_input == 'search':
            tasks = load_json(TASK_FILE)

            date_input: str = input("Enter date (yyyy-mm-dd): ")

            # Calls the function
            search_by_date(date_input, tasks)

        # Delete a task by their id
        elif chosen_input == 'delete':
            tasks = load_json(TASK_FILE)

            id_input = input("Enter id: ")

            result = [task["id"] for task in tasks if task["id"] == int(id_input)]

            if result:
                # Calls functions
                delete_task(int(id_input), tasks)
                save_list(tasks, TASK_FILE)

                print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} deleted successfully ═══════════════\n")

            else:
                print(Fore.RED + f"No task found with that ID.")

        # Show menu
        elif chosen_input == 'help':
            show_menu()
        # Else
        else:
            print("⚠ Invalid command. Try 'add', 'view', 'view_all', 'search', 'delete', 'help' or 'quit'.")

if __name__ == '__main__':
    main()