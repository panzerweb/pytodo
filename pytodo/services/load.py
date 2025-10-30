from datetime import date
from colorama import Fore, Style, init
init(autoreset=True)

# Load tasks for today
def view_task_today(arr, current_date):
    today_tasks = [task for task in arr if task["created_at"] == str(current_date)]

    if today_tasks:
        for i, task in enumerate(today_tasks, start=1):
            print(Fore.YELLOW + f"🗓  Task {i}")
            print(Fore.WHITE + f"   • Task ID     : {task['id']}")
            print(f"   • Title : {task['todo']}")
            print(f"   • Description : {task['description']}")
            print(f"   • Created At  : {task['created_at']}")
            print(Fore.CYAN + "────────────────────────────────────────────────────────────")
        print(Fore.GREEN + Style.BRIGHT + f"\n✅ {len(today_tasks)} task(s) for today ({current_date})\n")
    else:
        print(Fore.RED + "😴 No tasks for today.")
        print(Fore.LIGHTBLACK_EX + f"   Date checked: {current_date}\n")

def view_all(arr):
    all_tasks = [task for task in arr]
    # Sets current date
    get_date = date.today()

    if all_tasks:
        for i, task in enumerate(all_tasks, start=1):
            print(Fore.YELLOW + f"🗓  Task {i}")
            print(Fore.WHITE + f"   • Task ID     : {task['id']}")
            print(f"   • Title : {task['todo']}")
            print(f"   • Description : {task['description']}")
            print(f"   • Created At  : {task['created_at']}")
            print(Fore.CYAN + "────────────────────────────────────────────────────────────")
        print(Fore.GREEN + Style.BRIGHT + f"\n✅ You have a total of {len(all_tasks)} task(s) | ({str(get_date)})\n")
    else:
        print(Fore.RED + "😴 No tasks for today.")
        print(Fore.LIGHTBLACK_EX + f"   Date checked: {str(get_date)}\n")

        