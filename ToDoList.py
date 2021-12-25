from datetime import date 
import Priority
from Task import Task 

class toDoList:
    def __init__(self, Tasks, ListName):
        self.Tasks=Tasks
        self.ListName= ListName

listname = str(input())
TaskName=str(input())
Date= int(input())
Category= str(input())
PriorityLevel= str(input())
task= Task(Date, Category, PriorityLevel, TaskName)
tasks=[]
tasks.append(task)
task.Add()
todolist=toDoList(tasks, listname)
