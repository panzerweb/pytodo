from colorama import init, Fore, Style

def show_commands():
    print(Fore.YELLOW + Style.BRIGHT + "\nHi! Welcome to " + Fore.CYAN + "PyTodo 👋\n")
    print(Fore.GREEN + "Available Commands:")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'add'" + Fore.WHITE + "     → Insert a new task")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'edit_task'" + Fore.WHITE + "     → Edit a task")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'view'" + Fore.WHITE + "    → Show all tasks for today")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'view_all'" + Fore.WHITE + "    → Show all tasks")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'yest_view'" + Fore.WHITE + "    → Show all tasks yesterday")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'search_date'" + Fore.WHITE + "  → Search tasks by date")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'delete'" + Fore.WHITE + "  → Delete a task by ID")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'help'" + Fore.WHITE + "  → Show all commands")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'quit'" + Fore.WHITE + "    → Exit the program\n")
    print(Fore.LIGHTBLACK_EX + "────────────────────────────────────────────────────────")

if __name__ == "__main__":
    show_commands()