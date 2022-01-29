class Task:
   def __init__(self, Date, Category, PriorityLevel, TaskName):
    self.TaskName= TaskName
    self.Date= Date
    self. Category=Category
    self. PriorityLevel= PriorityLevel

   def Add(self, filename):
       f=open(filename, 'a+')
       f.write("\n")
       f.write("Task Name:")
       f.write(self.TaskName)
       f.write("\n")
       f.write("Due date is:")
       f.write(str(self.Date))
       f.write("\n")
       f.write("Category:")
       f.write(self.Category)
       f.write("\n")
       f.write("Priority Level:")
       f.write(self.PriorityLevel)
       f.write("\n")
       f.write("\n")
       
   def Remind(self):
       currentdate=date.today()
       if(self.Date-currentdate<=1):
           print("Task Reminder ", self.TaskName)
        
