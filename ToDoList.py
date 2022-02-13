import datetime

from Task import Task

class toDoList:
    def __init__(self, Tasks, ListName):
        self.Tasks=Tasks
        self.ListName= ListName

while True:
    print(" Choose an option: ")
    print("\n")
    print("1. See a previous list ")
    print("2. Create a new list")
    print("3. Quit the program")
    UserInput=int(input())
    if(UserInput==1):
        print("What is the name of the list?")
        ListNameResponse=str(input())
        f=open(ListNameResponse, 'r')
        for line in f:    
            print(line)

    if UserInput==2:
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
            print("Task Added to List: "+ listname)
            print("Would you like to add another task? [y/n]")
            TaskResponse=str(input())
        todolist=toDoList(tasks, listname)

    if(UserInput==3):
        print("Thanks for coming, see you next time!")
        quit()
        