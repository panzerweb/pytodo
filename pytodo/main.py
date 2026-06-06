from datetime import date
from colorama import Fore, Style, init
import os

from pytodo.menu import *
from pytodo.utils.commands import *

# Services
from pytodo.services.task_cubit import createTask, readAllTask

init(autoreset=True)

def main():
    # init
    # clear_screen()
    # show_title()
    # show_menu()

    # Sets current date
    current_date = date.today()

    # Show Once the tasks yesterday
    # print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS TODAY ═══════════════════════\n")

    # Show tasks today
    

    # print(Fore.CYAN + Style.BRIGHT + "\n════════════════════════════════════════════════════════════════════\n")

    while True:
        chosen_input = input(Fore.CYAN + f"\nYour Command: ").strip().lower()

        if chosen_input == 'quit':
            break

        if chosen_input == 'add':
            taskName = input("Task name: ")
            taskDescription = input("Description: ")
            taskCategory = input("Category: ")

            createTask(taskName, taskDescription, taskCategory, current_date)
        
        elif chosen_input == 'read':
            readAllTask()

        else:
            print("⚠ Invalid command. Try 'add', 'update', 'view', 'view_all', 'yest_view', 'search_date', 'delete', 'help' or 'quit'.")


if __name__ == '__main__':
    main()