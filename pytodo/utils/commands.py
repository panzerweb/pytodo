from colorama import init, Fore, Style
from pytodo.models.command_entity import CommandDictionary

COMMANDS = [
    CommandDictionary("add", "Insert a new task"), #0
    CommandDictionary("update", "Update a task"), #1
    CommandDictionary("read", "Read all tasks"), #2
    CommandDictionary("delete", "Delete a task"), #3
    CommandDictionary("days_ago", "Read tasks by how many days ago"), #4
    CommandDictionary("toggle", "Toggle status of a task (complete or incomplete)"), #5
    CommandDictionary("bulk_add", "Add multiple tasks in one command"), #6
    CommandDictionary("search_date", "Search tasks by date"), #7
    CommandDictionary("help", "Show all commands"), #8
    CommandDictionary("stats", "Shows user statistics"), #9
    CommandDictionary("quit", "Exit the program"), #10
]

def show_commands():
    print(Fore.YELLOW + Style.BRIGHT + "\nHi! Welcome to " + Fore.CYAN + "PyTodo 👋\n")
    print(Fore.GREEN + "Available Commands:")

    for command in COMMANDS:
        print(Fore.WHITE + "Type " + Fore.CYAN + f"{command.action}" + Fore.WHITE + f"     → {command.description}")
    
    print(Fore.LIGHTBLACK_EX + "────────────────────────────────────────────────────────")

if __name__ == "__main__":
    show_commands()