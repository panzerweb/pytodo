from datetime import date, timedelta
from colorama import Fore, Style, init
init(autoreset=True)

# Handles the display of data in a clean, readable format

# Load tasks for today
def view_task_today(arr: list, current_date: str) -> None:
    # return [task for task in arr if task["created_at"] == str(current_date)]

    # DEPRECETAED - GUI now handles display

    # RESTORED - CLI still handles display
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

# Displays today stats
def today_tasks_count(arr: list, current_date: str) -> None:
    today_tasks = [task for task in arr if task["created_at"] == str(current_date)]

    print(f"Good day!")
    print(f"\n📅 Tasks for {current_date}")
    print("-" * 30)

    if not today_tasks:
        print("✅ No tasks scheduled for today. Type 'add' to create some task")
        return

    print(f"📝 You have {len(today_tasks)} task(s) today. Stay focused!")

# Load all tasks
def view_all(arr: list) -> None:
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

# Load tasks yesterday
def view_yesterday(arr: list, current_date: str) -> None:
    yesterday_date = current_date - timedelta(days=1)
    yesterday_tasks = [task for task in arr if task["created_at"] == str(yesterday_date)]

    if yesterday_tasks:
        for i, task in enumerate(yesterday_tasks, start=1):
            print(Fore.YELLOW + f"🗓  Task {i}")
            print(Fore.WHITE + f"   • Task ID     : {task['id']}")
            print(f"   • Title : {task['todo']}")
            print(f"   • Description : {task['description']}")
            print(f"   • Created At  : {task['created_at']}")
            print(Fore.CYAN + "────────────────────────────────────────────────────────────")
        print(Fore.GREEN + Style.BRIGHT + f"\n✅ {len(yesterday_tasks)} task(s) for yesterday ({yesterday_date})\n")
    else:
        print(Fore.RED + "😴 No tasks yesterday.")
        print(Fore.LIGHTBLACK_EX + f"   Date checked: {yesterday_date}\n")
        