import itertools
from colorama import Fore, Style, init

init(autoreset=True)

class List:
    # Initializes data models for class List
    def __init__(self, id, uuid, todos, description, created_at = '00-00-0000'):
        self.__id = id
        self.__uuid = uuid
        self.__todos = todos
        self.__description = description
        self.__created_at = created_at

    # Convert to dictionary
    def to_dict(self):
        return {
            "id": self.__id,
            "uuid": self.__uuid,
            "todo": self.__todos,
            "description": self.__description,
            "created_at": self.__created_at
        }
    
    def display_list(self):
        print(Fore.GREEN + Style.BRIGHT + "\n🎉 TASK CREATED SUCCESSFULLY 🎉")
        print(Fore.CYAN + "═══════════════════════════════════════════════")
        print(Fore.WHITE + f"🗒️  Task       : {self.__todos}")
        print(Fore.WHITE + f"🗒️  Description       : {self.__description}")
        print(f"📅 Created At : {self.__created_at}")
        print(f"🆔 Task ID    : {self.__id}")
        print(f"🔑 UUID       : {self.__uuid}")
        print(Fore.CYAN + "═══════════════════════════════════════════════")
        print(Fore.LIGHTBLACK_EX + "💡 Tip: Type 'view' to display all tasks for today.\n")
