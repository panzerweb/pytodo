from pytodo.models.task_entity import TaskEntity, TaskUpdateDTO
from pytodo.json_services import *
from pytodo.data.app_services import create, read, update, delete
from pytodo.utils.object_cleaner import clean
from datetime import date, timedelta
from colorama import Fore, Style, init
import pandas as pd
import math

# Defines the current date
current_date = date.today()

# Creating task cubit
def createTask(taskName: str, description: str, category: str) -> None:
    if taskName == '' or description == '' or category == '':
        print("Please fill all the fields required")
        return
    
    taskEntity: TaskEntity = TaskEntity(taskName, category, current_date, description)

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

# Reading all tasks by days ago
def readTaskByDaysAgo(days: int) -> None:
    yesterday_date = current_date - timedelta(days=days)
    
    tasks: list[TaskEntity] = read(dateParams=str(yesterday_date))

    if len(tasks) == 0:
        print("Empty tasks, check message or create one")

    print(Fore.YELLOW + Style.BRIGHT + f"===== Display Tasks {days} days ago =====")

    df = pd.DataFrame([task.to_dict() for task in tasks])

    print(df);

    print(Fore.YELLOW + Style.BRIGHT + "=============================")

# Reading all task by a specific date
def searchTasksByDate(specifiedDate: str) -> None:
    # Add a validation to reject if the string is not a valid format of yyyy-mm-dd
    

    tasks: list[TaskEntity] = read(dateParams=specifiedDate)

    if len(tasks) == 0:
        print("Empty tasks, check message or create one")

    print(Fore.YELLOW + Style.BRIGHT + f"===== Display Tasks for {specifiedDate} =====")

    df = pd.DataFrame([task.to_dict() for task in tasks])

    print(df);

    print(Fore.YELLOW + Style.BRIGHT + "=============================")

# Updating a task
def updateTask(taskId: int, taskName: str = None, description: str = None, category: str = None, status: str = None):
    statusLabel: str = None

    if math.isnan(taskId):
        print("Task Id provided is NaN (Not a Number)")
        return

    if status == 'y':
        statusLabel = 'complete'
    elif status == 'n':
        statusLabel = 'incomplete'

    newTask = TaskUpdateDTO(name=clean(taskName), description=clean(description), category=clean(category), status=clean(statusLabel))

    result = update(taskId, newTask)

    print(result)

    
# Toggling a task
def toggleTask(taskId: int, status: str = None):
    statusLabel: str = None

    if math.isnan(taskId):
        print("Task Id provided is NaN (Not a Number)")
        return
    
    if status == 'y':
        statusLabel = 'complete'
    elif status == 'n':
        statusLabel = 'incomplete'
    
    taskToggle = TaskUpdateDTO(name=None, description=None, category=None, status=clean(statusLabel))

    result = update(taskId=taskId, task=taskToggle)

    print(result)

# Toggle a task for today
def toggleTaskToday():
    print("Toggle Tasks for today")

# Deleting a task
def deleteTask(taskId: int):
    if taskId == None:
        print("Please provide an id")

    if delete(taskId):
        print("Task deleted successfully")
    else:
        print("Task deletion failed")
