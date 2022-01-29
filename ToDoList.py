import datetime

from Task import Task

class toDoList:
    def __init__(self, Tasks, ListName):
        self.Tasks=Tasks
        self.ListName= ListName

print("Would you like to see a previous list? [y/n]")
PrevListResponse=str(input())
if(PrevListResponse=="y"):
    print("What is the name of the list?")
    ListNameResponse=str(input())
    f=open(ListNameResponse, 'r')
    for line in f:    
        print(line)

print("Would you like to create a new list? [y/n]")
ListResponse=str(input())
if ListResponse=="y":
    print("What is the name of the list?")
    listname = str(input())
    tasks=[]
    print("Would you like to add a task? [y/n]")
    TaskResponse=str(input())
    while TaskResponse=="y":
        print ("What's the name of the task?")
        TaskName=str(input())
        print("When do want this to be done by?(Month number)")
        Month=int(input())
        print("What date in the month?")
        Day= int(input())
        print("What year?")
        Year=int(input())
        print("What hour?")
        Hour=int(input())
        Date=datetime.datetime(Year, Month, Day, Hour)
        print("What category would you like to place this in? ex: hw, science project, etc.")
        Category= str(input())
        print("How important is this task to finish? (High/moderate/low)")
        PriorityLevel= str(input())
        task= Task(Date, Category, PriorityLevel, TaskName)
        tasks.append(task)
        task.Add(listname)
        print("Would you like to add another task? [y/n]")
        TaskResponse=str(input())
    todolist=toDoList(tasks, listname)
