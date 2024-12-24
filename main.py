import random
import uuid
import sqlite3 as dbs
import json
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

def openDB(taskName, id, description, status, dateStart, dateUpdate):
  nmTask = [0];
  arrayList = {
    f"Task{nmTask.append()}"
    "Task name": taskName,
    "Task ID": id,
    "Description": description,
    "Status": status,
    "DaT": dateStart,
    "DaU": dateUpdate,
  }
  with open("databaseCrud.json", "r+") as db:
    if db.readline() == "}":
      db.write('\n');
    jsConvert = json.dumps(arrayList)
    db.write(jsConvert)

openDB("taskName", "id", "description", "status", "dateStart", "dateUpdate")

exit()

if(opt == ""):
  print("Please write something!!")

elif(opt == "1"):
  print("Sure, answer that questions: ");
  taskID = uuid.uuid1();
  taskName = input("Task Name: ");
  taskDescription = input("Please, talk about your task: ");
  pass