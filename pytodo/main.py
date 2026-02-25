from pytodo.services.create_task import create_list
from pytodo.services.json_services import *
from pytodo.services.delete_task import delete_task
from pytodo.services.search_task import search_by_date
from pytodo.services.display_tasks import *
from pytodo.services.update_task import update_task
from datetime import date
from colorama import Fore, Style, init
import os

from pytodo.menu import *
from pytodo.utils.commands import *

init(autoreset=True)

# get the directory of the current script (main.py)
BASE_DIR = os.path.dirname(__file__)
TASK_FILE = os.path.join(BASE_DIR, 'tasks.json')

# Global variable - Load JSON file and its data
TASKS_LOADED = load_json(TASK_FILE)

def main():
    # init
    clear_screen()
    show_title()
    show_menu()

    # Sets current date
    current_date = date.today()

    # Show Once the tasks yesterday
    print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS YESTERDAY ═══════════════════════\n")

    view_yesterday(TASKS_LOADED, current_date)

    print(Fore.CYAN + Style.BRIGHT + "\n════════════════════════════════════════════════════════════════════\n")

    while True:
        chosen_input = input("\nYour Command: ").strip().lower()

        if chosen_input == 'quit':
            break
        
        # Add a task
        elif chosen_input == 'add':
            task_input = input("Task name: ")
            desc_input = input("Description: ")

            # Execute function
            create_list(task_input, desc_input, str(current_date))

        # Edit a task
        elif chosen_input == 'edit_task':
            id_input = input("Enter id: ")

            result = [task["id"] for task in TASKS_LOADED if task["id"] == int(id_input)]

            if result:
                new_todo = input("Enter new todo: ")
                new_description = input("Enter new description: ")

                update_task(int(id_input), new_todo, new_description)
                print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} updated successfully ═══════════════\n")

            else:
                print(Fore.RED + f"No task found with that ID.")

        # View all tasks for today
        elif chosen_input == 'view':
            if not TASKS_LOADED:
                print(Fore.LIGHTBLACK_EX + "📭 No tasks yet.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS FOR TODAY ═══════════════════════\n")

                # Calls the function
                view_task_today(TASKS_LOADED, current_date)

        # View all tasks
        elif chosen_input == 'view_all':
            if not TASKS_LOADED:
                print(Fore.LIGHTBLACK_EX + "📭 You have no tasks at all.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS ═══════════════════════\n")

                # Calls the function
                view_all(TASKS_LOADED)
        
        # View all tasks yesterday
        elif chosen_input == 'yest_view':
            if not TASKS_LOADED:
                print(Fore.LIGHTBLACK_EX + "📭 You have no tasks yesterday.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS YESTERDAY ═══════════════════════\n")

                # Calls the function
                view_yesterday(TASKS_LOADED, current_date)

        # Search task by date (yyyy-mm-dd)
        elif chosen_input == 'search':
            date_input: str = input("Enter date (yyyy-mm-dd): ")

            # Calls the function
            search_by_date(date_input, TASKS_LOADED)

        # Delete a task by their id
        elif chosen_input == 'delete':
            id_input = input("Enter id: ")

            result = [task["id"] for task in TASKS_LOADED if task["id"] == int(id_input)]

            if result:
                # Calls functions
                delete_task(int(id_input), TASKS_LOADED)
                save_list(TASKS_LOADED, TASK_FILE)

                print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} deleted successfully ═══════════════\n")

            else:
                print(Fore.RED + f"No task found with that ID.")

        # Show menu
        elif chosen_input == 'help':
            show_commands()
        # Else
        else:
            print("⚠ Invalid command. Try 'add', 'edit_task', 'view', 'view_all', 'yest_view', 'search', 'delete', 'help' or 'quit'.")

if __name__ == '__main__':
    main()