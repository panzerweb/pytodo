from pytodo.services.create_task import create_list
from pytodo.json_services import *
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
# TASKS_LOADED = load_json(TASK_FILE)


def main():
    TASKS_LOADED = load_tasks()
    # init
    clear_screen()
    show_title()
    show_menu()

    # Sets current date
    current_date = date.today()

    # Show Once the tasks yesterday
    print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS TODAY ═══════════════════════\n")

    # view_yesterday(TASKS_LOADED, current_date)
    today_tasks_count(TASKS_LOADED, current_date)

    print(Fore.CYAN + Style.BRIGHT + "\n════════════════════════════════════════════════════════════════════\n")

    while True:
        chosen_input = input(Fore.CYAN + f"\nYour Command: ").strip().lower()

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
            try:
                refreshed_tasks = load_tasks()
                id_input = input("Enter id: ")

                result = [task["id"] for task in refreshed_tasks if task["id"] == int(id_input)]

                if result:
                    new_todo = input("Enter new todo: ")
                    new_description = input("Enter new description: ")

                    update_task(refreshed_tasks, int(id_input), new_todo, new_description)
                    save_tasks(refreshed_tasks)
                    print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} updated successfully ═══════════════\n")
                else:
                    print(Fore.RED + f"No task found with that ID.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        # View all tasks for today
        elif chosen_input == 'view':
            refreshed_tasks = load_tasks()
            if not refreshed_tasks:
                print(Fore.LIGHTBLACK_EX + "📭 No tasks yet.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS FOR TODAY ═══════════════════════\n")

                # Calls the function
                view_task_today(refreshed_tasks, current_date)

        # View all tasks
        elif chosen_input == 'view_all':
            refreshed_tasks = load_tasks()
            if not refreshed_tasks:
                print(Fore.LIGHTBLACK_EX + "📭 You have no tasks at all.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS ═══════════════════════\n")

                # Calls the function
                view_all(refreshed_tasks)
        
        # View all tasks yesterday
        elif chosen_input == 'yest_view':
            refreshed_tasks = load_tasks()
            if not refreshed_tasks:
                print(Fore.LIGHTBLACK_EX + "📭 You have no tasks yesterday.\n")
            else:
                print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS YESTERDAY ═══════════════════════\n")

                # Calls the function
                view_yesterday(refreshed_tasks, current_date)

        # Search task by date (yyyy-mm-dd)
        elif chosen_input == 'search_date':
            refreshed_tasks = load_tasks()
            date_input: str = input("Enter date (yyyy-mm-dd): ")

            # Calls the function
            search_by_date(date_input, refreshed_tasks)

        # Delete a task by their id
        elif chosen_input == 'delete':
            try:
                refreshed_tasks = load_tasks()
                id_input = input("Enter id: ")

                result = [task["id"] for task in refreshed_tasks if task["id"] == int(id_input)]

                if result:
                    # Calls functions
                    delete_task(int(id_input), refreshed_tasks)
                    # save_list(TASKS_LOADED, TASK_FILE)
                    save_tasks(refreshed_tasks)

                    print(Fore.GREEN + Style.BRIGHT + f"\n═══════════════ Task Id: {id_input} deleted successfully ═══════════════\n")

                else:
                    print(Fore.RED + f"No task found with that ID.")            
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        # Show menu
        elif chosen_input == 'help':
            show_commands()
        # Else
        else:
            print("⚠ Invalid command. Try 'add', 'edit_task', 'view', 'view_all', 'yest_view', 'search_date', 'delete', 'help' or 'quit'.")

if __name__ == '__main__':
    main()