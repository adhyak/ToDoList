class Task:
   def __init__(self, Date, Category, PriorityLevel, TaskName):
    self.TaskName= TaskName
    self.Date= Date
    self. Category=Category
    self. PriorityLevel= PriorityLevel
    self.TASK_FILE='tasks'
  
   def Add(self):
       f=open(self.TASK_FILE, 'w+')
       f.write(self.TaskName)
       f.write(str(self.Date))
       f.write(self.Category)
       f.write(self.PriorityLevel)


   def Remind(self):
       currentdate=date.today()
       if(self.Date-currentdate<=1):
           print("Task Reminder ", self.TaskName)
        
