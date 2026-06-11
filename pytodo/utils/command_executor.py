from pytodo.modules.app_modules import *
from pytodo.utils.commands import *

def execute_command(command: str):

    if command == COMMANDS[11].action:
        print("Quitting...")
        return False

    if command == COMMANDS[0].action:
        addTaskModule()

    elif command == COMMANDS[1].action:
        updateTaskModule()

    elif command == COMMANDS[2].action:
        readAllTasksModule()
    
    elif command == COMMANDS[3].action:
        deleteTaskModule()

    elif command == COMMANDS[4].action:
        readTaskByDaysAgoModule()

    elif command == COMMANDS[5].action:
        toggleTaskModule()

    elif command == COMMANDS[6].action:
        findTasksByCategoryOrStatusModule()

    elif command == COMMANDS[7].action:
        bulkAddTaskModule()

    elif command == COMMANDS[8].action:
        searchTasksByDateModule()

    elif command == COMMANDS[9].action:
        showHelpCommandModule()

    elif command == COMMANDS[10].action:
        getStatsCountModule()

    return True