from datetime import date
from colorama import Fore, Style, init
import os

from pytodo.menu import *
from pytodo.utils.commands import *

# Services
from pytodo.services.task_cubit import createTask, readAllTask, updateTask, deleteTask, readTaskByDaysAgo, searchTasksByDate, toggleTask

init(autoreset=True)

def main():
    # init
    clear_screen()
    show_title()
    show_commands()

    # Show Once the tasks yesterday
    print(Fore.CYAN + Style.BRIGHT + "\n═══════════════════════ YOUR TASKS TODAY ═══════════════════════\n")

    # Show tasks today
    readTaskByDaysAgo(days=0)

    print(Fore.CYAN + Style.BRIGHT + "\n════════════════════════════════════════════════════════════════════\n")

    while True:
        chosen_input = input(Fore.CYAN + f"\nYour Command: ").strip().lower()
    
        if chosen_input == COMMANDS[10].action:
            break

        if chosen_input == COMMANDS[0].action:
            taskName = input("Task name: ")
            taskDescription = input("Description: ")
            taskCategory = input("Category: ")

            createTask(taskName, taskDescription, taskCategory)

        elif chosen_input == COMMANDS[1].action:
            try:
                taskId = int(input('Task Id: ').strip())
                taskName = input('Name: ').strip()
                taskDescription = input("Description: ").strip()
                taskCategory = input("Category: ").strip()
                taskStatus = input("Toggle status (y/n): ").lower().strip()

                updateTask(taskId, taskName, taskDescription, taskCategory, taskStatus)
            except ValueError:
                print("Task Id input is not an integer")
        
        
        elif chosen_input == COMMANDS[2].action:
            readAllTask()
        
        elif chosen_input == COMMANDS[3].action:
            try:
                taskId = int(input('Task Id: ').strip())

                deleteTask(taskId=taskId)
            
            except ValueError:
                print("Task Id input is not an integer")
        
        elif chosen_input == COMMANDS[4].action:
            try:
                days_ago_input = int(input("How many days ago: ").strip())

                readTaskByDaysAgo(days=days_ago_input)
            except ValueError:
                print("Input is not an integer")

        elif chosen_input == COMMANDS[5].action:
            print("Toggle task")
            try:
                taskId = int(input('Task Id: ').strip())
                taskStatus = input("Toggle status (y/n): ").lower().strip()

                toggleTask(taskId=taskId, status=taskStatus)
            
            except ValueError:
                print("Task Id input is not an integer")

        elif chosen_input == COMMANDS[6].action:
            print("Bulk add still under development")
        
        elif chosen_input == COMMANDS[7].action:
            specificDate = input("Enter date (yyyy-mm-dd): ")
            
            searchTasksByDate(specifiedDate=specificDate)

        elif chosen_input == COMMANDS[8].action:
            show_commands()

        elif chosen_input == COMMANDS[9].action:
            print("User statistics still under development")

        else:
            print("⚠ Invalid command. Try 'add', 'update', 'view', 'view_all', 'yest_view', 'search_date', 'delete', 'help' or 'quit'.")


if __name__ == '__main__':
    main()