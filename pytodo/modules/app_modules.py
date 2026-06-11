# This will be functions that will reduce the massive if-elif-else statement
# in the main.py
from pytodo.services.task_cubit import createTask, bulkAddTasks, readAllTask, updateTask, deleteTask, readTaskByDaysAgo, searchTasksByDate, toggleTask, findTasksByCategoryOrStatus, showFirstTaskDetails
from pytodo.services.statistics_cubit import getStatistics
from pytodo.models.task_entity import TaskCreateDTO
from pytodo.utils.commands import *

def addTaskModule():
    taskName = input("Task name: ")
    taskDescription = input("Description: ")
    taskCategory = input("Category: ")

    createTask(taskName, taskDescription, taskCategory)

def bulkAddTaskModule():
    try:
        tasks_count = int(input("How many tasks: ").strip())
        listOfTasks: list[TaskCreateDTO] = []

        for i in range(tasks_count):
            print(f"Creating Task {i + 1}")

            taskName = input("Task name: ")
            taskDescription = input("Description: ")
            taskCategory = input("Category: ")

            if taskName == '' or taskDescription == '' or taskCategory == '':
                print("Please fill all the fields required")
                break

            listOfTasks.append(TaskCreateDTO(name=taskName, description=taskDescription, category=taskCategory))

        bulkAddTasks(listOfTasks)
    except ValueError:
        print("What you input is not an integer")

def updateTaskModule():
    try:
        taskId = int(input('Task Id: ').strip())
        
        showFirstTaskDetails(taskId=taskId)

        taskName = input('Name: ').strip()
        taskDescription = input("Description: ").strip()
        taskCategory = input("Category: ").strip()
        taskStatus = input("Toggle status (y/n): ").lower().strip()

        updateTask(taskId, taskName, taskDescription, taskCategory, taskStatus)
    except ValueError:
        print("Task Id input is not an integer")

def deleteTaskModule():
    try:
        taskId = int(input('Task Id: ').strip())

        showFirstTaskDetails(taskId=taskId)

        deleteTask(taskId=taskId)
    
    except ValueError:
        print("Task Id input is not an integer")

def readAllTasksModule():
    readAllTask()

def readTaskByDaysAgoModule():
    try:
        days_ago_input = int(input("How many days ago: ").strip())

        readTaskByDaysAgo(days=days_ago_input)
    except ValueError:
        print("Input is not an integer")

def searchTasksByDateModule():
    specificDate = input("Enter date (yyyy-mm-dd): ")
            
    searchTasksByDate(specifiedDate=specificDate)

def findTasksByCategoryOrStatusModule():
    category = input("Find Category: ").lower().strip()
    status = input("Find Status (complete or incomplete): ").lower().strip()

    if category == '' or status == '':
        print("Empty filter, can't return tasks")
        return

    findTasksByCategoryOrStatus(category=category, status=status)

def toggleTaskModule():
    print("Toggle task")
    try:
        taskId = int(input('Task Id: ').strip())

        showFirstTaskDetails(taskId=taskId)

        taskStatus = input("Toggle status as complete? (y/n): ").lower().strip()

        toggleTask(taskId=taskId, status=taskStatus)
    
    except ValueError:
        print("Task Id input is not an integer")

def getStatsCountModule():
    getStatistics()

def showHelpCommandModule():
    show_commands()

