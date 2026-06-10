from colorama import init, Fore, Style
from pytodo.models.command_entity import CommandDictionary

COMMANDS = [
    CommandDictionary(
        "add",
        "Insert a new task",
        ["add", "create", "insert", "new"]
    ),

    CommandDictionary(
        "update",
        "Update a task",
        ["update", "edit", "modify"]
    ),

    CommandDictionary(
        "read",
        "Read all tasks",
        ["read", "show", "list", "display", "view"]
    ),

    CommandDictionary(
        "delete",
        "Delete a task",
        ["delete", "remove", "erase"]
    ),

    CommandDictionary(
        "days_ago",
        "Read tasks by how many days ago",
        ["days ago", "yesterday"]
    ),

    CommandDictionary(
        "toggle",
        "Toggle status of a task",
        ["toggle", "complete", "incomplete", "finish"]
    ),

    CommandDictionary(
        "bulk_add",
        "Add multiple tasks in one command",
        ["bulk", "multiple"]
    ),

    CommandDictionary(
        "search_date",
        "Search tasks by date",
        ["search", "find date"]
    ),

    CommandDictionary(
        "help",
        "Show all commands",
        ["help", "commands"]
    ),

    CommandDictionary(
        "stats",
        "Shows user statistics",
        ["stats", "statistics"]
    ),

    CommandDictionary(
        "quit",
        "Exit the program",
        ["quit", "exit", "close"]
    ),
]

def show_commands():
    print(Fore.YELLOW + Style.BRIGHT + "\nHi! Welcome to " + Fore.CYAN + "PyTodo 👋\n")
    print(Fore.GREEN + "Available Commands:\n")

    for command in COMMANDS:
        natural = ", ".join(command.natural_lang)

        print(
            Fore.CYAN + f"{command.action:<12}"
            + Fore.WHITE + f"→ {command.description}"
        )

        print(
            Fore.LIGHTBLACK_EX + f"   Voice: {natural}"
        )

    print(Fore.LIGHTBLACK_EX + "\n────────────────────────────────────────────────────────")

if __name__ == "__main__":
    show_commands()