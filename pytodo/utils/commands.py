from colorama import init, Fore, Style
from pytodo.models.command_entity import CommandDictionary

COMMANDS = [
    CommandDictionary(
        "add",
        "Insert a new task",
        ["add task", "create task", "insert task", "new task", "add a task", "create a task", "insert a task"]
    ), # 0

    CommandDictionary(
        "update",
        "Update a task",
        ["update task", "edit a task", "modify a task", "update a task", "edit a task", "modify a task"]
    ), # 1

    CommandDictionary(
        "read",
        "Read all tasks",
        ["read all", "show all", "list all", "display all", "view all"]
    ), # 2

    CommandDictionary(
        "delete",
        "Delete a task",
        ["delete", "remove", "erase", "delete a task", "remove task", "remove a task", "erase task"]
    ), # 3

    CommandDictionary(
        "days_ago",
        "Read tasks by how many days ago",
        ["recent task", "recent task","task from last days", "task from days ago"]
    ), # 4

    CommandDictionary(
        "toggle",
        "Toggle status of a task",
        ["toggle task", "mark a task", "mark task", "mark task", "toggle task"]
    ), # 5

    CommandDictionary(
        "find_cat_stat",
        "Find tasks by category or status",
        ["find category", "find status", "find task", "find"]
    ), # 6
    

    CommandDictionary(
        "bulk_add",
        "Add multiple tasks in one command",
        ["create many", "insert many","create multiple", "insert multiple","add multiple task", "bulk add task", "create many task", "insert multiple task"]
    ), # 7

    CommandDictionary(
        "search_date",
        "Search tasks by date",
        ["search by date","search task by date", "find task by date", "task on date", "filter by date"]
    ), # 8

    CommandDictionary(
        "help",
        "Show all commands",
        ["help", "show commands", "list commands", "what can I do", "available commands", 'assist']
    ), # 9

    CommandDictionary(
        "stats",
        "Shows user statistics",
        ["show stat", "show stats", "show my stats", "show statistics", "stats", "statistics"]
    ), # 10

    CommandDictionary(
        "quit",
        "Exit the program",
        ["quit", "exit", "close"]
    ), # 11
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
            Fore.LIGHTBLACK_EX + f"   Voice: {natural} \n"
        )

    print(Fore.YELLOW + Style.BRIGHT + "Caution: " + Fore.GREEN + "This is a rule-based command, please follow the suggested prompts when doing either voice or non-voice command. \n")
    print(Fore.LIGHTBLACK_EX + "\n────────────────────────────────────────────────────────")

if __name__ == "__main__":
    show_commands()