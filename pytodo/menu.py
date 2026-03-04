from colorama import init, Fore, Style
import os

init(autoreset=True)

# Clear previous commands in CLI whenever program is start
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    print(Fore.GREEN + Style.BRIGHT + r"""
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                                                                           ║
    ║    ░█████████                ░██                      ░██                 ║
    ║    ░██     ░██               ░██                      ░██                 ║
    ║    ░██     ░██ ░██    ░██ ░████████  ░███████   ░████████  ░███████       ║
    ║    ░█████████  ░██    ░██    ░██    ░██    ░██ ░██    ░██ ░██    ░██      ║
    ║    ░██         ░██    ░██    ░██    ░██    ░██ ░██    ░██ ░██    ░██      ║
    ║    ░██         ░██   ░███    ░██    ░██    ░██ ░██   ░███ ░██    ░██      ║
    ║    ░██          ░█████░██     ░████  ░███████   ░█████░██  ░███████       ║
    ║                       ░██                                                 ║
    ║                 ░███████                                                  ║
    ║                                                                           ║
    ║                                        Your Personal Boot Todo            ║
    ╚═══════════════════════════════════════════════════════════════════════════╝

    ==============================================================================
          __   __          __        __     ___       __       
    ╦ ╦┬ ┬┌─┐┌┬┐  ┌─┐┬─┐┌─┐  ┬ ┬┌─┐┬ ┬  ┌─┐┌─┐┌┐┌┌┐┌┌─┐  ┌┬┐┌─┐  ┌┬┐┌─┐┌┬┐┌─┐┬ ┬┌─┐
    ║║║├─┤├─┤ │   ├─┤├┬┘├┤   └┬┘│ ││ │  │ ┬│ │││││││├─┤   │││ │   │ │ │ ││├─┤└┬┘ ┌┘
    ╚╩╝┴ ┴┴ ┴ ┴   ┴ ┴┴└─└─┘   ┴ └─┘└─┘  └─┘└─┘┘└┘┘└┘┴ ┴  ─┴┘└─┘   ┴ └─┘─┴┘┴ ┴ ┴  o 

    ==============================================================================                                                      
    """)

    
def show_menu():
    print(Fore.YELLOW + Style.BRIGHT + "\nHi! Welcome to " + Fore.CYAN + "PyTodo 👋\n")
    print(Fore.GREEN + "Available Commands:")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'add'" + Fore.WHITE + "     → Insert a new task")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'edit_task'" + Fore.WHITE + "     → Edit a task")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'view'" + Fore.WHITE + "    → Show all tasks for today")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'search_date'" + Fore.WHITE + "  → Search tasks by date")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'delete'" + Fore.WHITE + "  → Delete a task by ID")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'help'" + Fore.WHITE + "  → Show all commands")
    print(Fore.WHITE + "Type " + Fore.CYAN + "'quit'" + Fore.WHITE + "    → Exit the program\n")

    print(Fore.LIGHTBLACK_EX + "────────────────────────────────────────────────────────")
    print(Fore.WHITE + "Type 'help' to show more commands.")
    print(Fore.LIGHTBLACK_EX + "────────────────────────────────────────────────────────")

if __name__ == "__main__":
    clear_screen()
    show_title()
    show_menu()