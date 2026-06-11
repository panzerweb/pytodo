from datetime import date
from colorama import Fore, Style, init
import os

from pytodo.config.database import activateDb
from pytodo.menu import *
from pytodo.utils.commands import *

# Services
from pytodo.modules.app_modules import *
from pytodo.services.speech_to_text_cubit import voiceCommand

# Models
from pytodo.models.task_entity import TaskCreateDTO

# Utils
from pytodo.utils.get_user_input import get_user_input
from pytodo.utils.command_executor import execute_command
from pytodo.utils.command_parser import parse_command

init(autoreset=True)

def main():
    # init
    activateDb() # Activate Database and Create the Table if not exist
    clear_screen()
    show_title()
    show_commands()

    # Activate Voice Command Module
    print("Voice Mode uses Google Web Speech API, so it is not suitable for offline usage")
    voice_mode = (input("Enable voice mode (y/n): ").lower().strip() == "y")

    # Show Once the tasks yesterday

    while True:
        raw_text = get_user_input(voice_mode=voice_mode)

        if not raw_text:
            continue

        command = parse_command(raw_text)

        print(f"Current command: {command}")

        if command is None:
            print("Unknown Command, please refer to the suggested prompts 'Voice' section")
            print("Type 'help', or 'assist' to show guide")
            continue

        action = execute_command(command=command)

        if action == False:
            break

        if not action:
            continue
        
if __name__ == '__main__':
    main()