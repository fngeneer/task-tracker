import json
import os
from datetime import datetime

#----------BASE FUNCTIONS----------#


def load_tasks():
    if not os.path.exists("table.json"):
        open("table.json", "w")
    with open("table.json", "r") as table:
        try:
            return json.load(table)
        except json.JSONDecodeError: 
            return []
        
def save_tasks(tasks):
    with open("table.json", "w") as table:
        json.dump(tasks, table, indent=4)

#----------OPERATIONAL FUNCTIONS----------#

def show_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task['id']} |{task['description']} |Status: {task['status']} |Created At: {task['createdAt']} |Updated At: {task['updatedAt']}")

def add_task(content):
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1

    new_task = {
        "id": task_id,
        "description": content,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print(f"Task added successfully (ID: {task_id})")

def delete_task(id):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == id:

            tasks.remove(task)

            save_tasks(tasks)

def update_task(id, new_content):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == id:
            task["descripton"] = new_content
            task["updatedAt"] = datetime.now().isoformat()

            save_tasks(tasks)
            return

def mark_task(task_id, status):
    if status not in ["in-progress", "done"]:
        print("Invalid status.")
        return
    
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status

            task['updatedAt'] = datetime.now().isoformat()

            save_tasks(tasks)

            return
        

"""print("All good")
load_tasks()
print("All good")"""

#create_table()

#           D:\Programming\Projects\applications\task_tracker\functions.py