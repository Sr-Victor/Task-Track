import random
import uuid


print("""

 Please, select a option:
  1 - Add task
  2 - Remove task
  3 - Update Task
  4 - List all tasks
  5 - List all tasks that are done
  6 - List all tasks that are not done
  7 - List all tasks that are in progress
""");

opt = input(": ")

if(opt == ""):
  print("Please write something!!")

elif(opt == "1"):
  print("Sure, answer that questions: ")
  taskID = uuid.uuid1();
  taskName = input("Task Name: ");
  print(f"This task id is: {taskID}")
  pass