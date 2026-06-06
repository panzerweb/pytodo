from pytodo.models.task_entity import TaskEntity
from pytodo.json_services import *
from pytodo.data.app_services import create, read
from datetime import date
from colorama import Fore, Style, init
import pandas as pd


# Creating task cubit
def createTask(taskName: str, description: str, category: str, currentDate: date) -> None:
    if taskName == '' or description == '' or category == '':
        print("Please fill all the fields required")
        return
    
    taskEntity: TaskEntity = TaskEntity(taskName, description, category, currentDate)

    if create(taskEntity):
        print("Successfully created task")
    else:
        print("Task creation failed")

# Reading all tasks cubit
def readAllTask() -> None:
    tasks: list[TaskEntity] = read()

    if len(tasks) == 0:
        print("Empty tasks, check message or create one")

    print(Fore.YELLOW + Style.BRIGHT + "===== Display All Tasks =====")

    df = pd.DataFrame([task.to_dict() for task in tasks])

    print(df);

    print(Fore.YELLOW + Style.BRIGHT + "=============================")

# Reading all tasks yesterday

# Reading all tasks today

# Updating a task

# Deleting a task