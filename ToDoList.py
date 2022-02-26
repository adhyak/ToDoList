import datetime
from Task import Task
import os

class toDoList:
    def __init__(self, Tasks, ListName):
        self.Tasks=Tasks
        self.ListName= ListName

def returnLines(ListName):
    f=open(ListName, 'r')
    return f.readlines()

def printList(ListName):
    f=open(ListName, 'r')
    for line in f:
        print(line)

while True:
    print(" Choose an option: ")
    print("\n")
    print("1. See a previous list ")
    print("2. Create a new list")
    print("3. Deleting a list")
    print("4. Delete a task")
    print("5. Quit the program")
    UserInput=int(input())
    
    if(UserInput==1):
        print("What is the name of the list?")
        ListNameResponse=str(input())
        printList(ListNameResponse)
        
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
        print("What list do you want to delete?")
        deleteFile=str(input())
        os.remove(deleteFile)
        print("\n")
        print("The list has been deleted!")
        print("\n")

    if(UserInput==4):
        print("From which list would you like to delete a task?")
        deleteListName=str(input())
        printList(deleteListName)
        lines = returnLines(deleteListName)
        print("Which task do you want to delete?")
        deleteTaskName=str(input())
        index=0
        totalLines = len(lines)
        for i in range (0,totalLines):
            if deleteTaskName in lines[i]:
                index=i
                break
        if(index==0):
            print("\n")
            print("Task not found!")
            print("\n")
        else:
            del lines[index-1:index+5]
            new_file = open(deleteListName, "w+")
            for line in lines:
                new_file.write(line)
            new_file.close()
            print("\n")
            print("Task succesfully deleted!")
            print("\n")

        


    if(UserInput==5):
        print("Thanks for coming, see you next time!")
        quit()
       