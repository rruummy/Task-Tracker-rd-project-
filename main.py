import time
import json
import os
import sys

def open_json():
    if not os.path.exists(JSON_PATH):
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        with open(JSON_PATH, "w") as data:
            pattern = {"LAST ID": 0, "TASKS": []}
            json.dump(pattern, data, indent=4)
    with open(JSON_PATH, "r") as data:
            return json.load(data)

def save_json(json_file):
    with open(JSON_PATH, "w") as data:
        json.dump(json_file, data, indent=4)

def print_task(task):
    print(f"ID: {task['ID']}")
    print(f"Name: {task['Name']}")
    print(f"Description: {task['Description']}")
    print(f"Status: {task['Status']}")  
    print(f"Date: {task['Date']}")
    print(f"Last change: {task['Last Change']}")
    print("-" * 20)

def search_task(id):
    tasks = open_json()
    for task in tasks["TASKS"]:
        if task["ID"] == id:
            return task
    return None

def list_tasks():
    tasks = open_json()
    print("-" * 20)
    for task in tasks["TASKS"]:
        print_task(task)
        
def create_task(name, description):
    json_file = open_json()
    task_name = name
    task_description = description
    task_creating_time = time.strftime("%d/%m/%y %H:%M:%S")
    task_id = json_file["LAST ID"] + 1
    json_file["TASKS"].append({
                       "ID": task_id,
                       "Name": task_name,
                       "Description": task_description,
                       "Status": "Created",
                       "Date": task_creating_time,
                       "Last Change": task_creating_time
    })
    json_file["LAST ID"] += 1
    print("Task created!")
    save_json(json_file)

def delete_task(id):
    try:
        json_file = open_json()
        ch_id = int(id)
        task = search_task(ch_id)
        if task != None:
            json_file["TASKS"].remove(task)
            save_json(json_file)
            print("Command done!")
        else:
            print("Task with this ID not found.") 
    except ValueError:
        print(f"You wrote invalid id or there`s not such id. Use command 'list' to show all id.")

def change_task_status(id, status):
    json_file = open_json()
    ch_status = status
    try:
        ch_id = int(id)
    except ValueError:
        print("Invalid ID.")
        return None
    
    if ch_status not in STATUSES:
        print("You wrote invalid status. ('Created', 'In progress', 'Done')")
        return None
    
    if search_task(ch_id):
        for task in json_file["TASKS"]:
            if task["ID"] == ch_id:
                task_change_time = time.strftime("%d/%m/%y %H:%M:%S")
                task["Status"] = ch_status
                task["Last Change"] = task_change_time
                save_json(json_file)
                print("Command done!")
    else:
        print("Task with this ID not found.") 

def change_task_name(id, name):
    json_file = open_json()
    task_new_name = name
    try:
        ch_id = int(id)
    except ValueError:
        print("Invalid ID.")
        return None
    if search_task(ch_id):
        for task in json_file["TASKS"]:
            if task["ID"] == ch_id:
                task_change_time = time.strftime("%d/%m/%y %H:%M:%S")
                task["Name"] = task_new_name
                task["Last Change"] = task_change_time
                print("Command done!")
        save_json(json_file)
    else:
        print("Task with this ID not found.") 

def filter_tasks(status):
    json_file = open_json()
    found = False
    fil_status = status
    if fil_status not in STATUSES:
        print("There`s not such status.(Write Created/In progress/Done)")
        return None
    for task in json_file["TASKS"]:
        if task["Status"] == fil_status:
            print_task(task)
            found = True
    if not found: print("Nothing.")


def show_help():
    print("=" * 20)
    print("List of commands:")
    print("create 'name' 'descption' - to create new task")
    print("delete 'id' - to delete task")
    print("list - show all tasks")
    print("schange 'id' 'Created/In progress/Done' - change a status of task")
    print("nchange 'id' 'name' - change a name of task")
    print("filter 'Created/In progress/Done'- show filtered tasks")
    print("=" * 20)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, "data", "tasks.json")
    STATUSES = ("Created", "In progress", "Done")
    try:
        if sys.argv[1] == "list":
            list_tasks()
        elif sys.argv[1] == "create":
            name = sys.argv[2]
            description = sys.argv[3] if len(sys.argv) > 3 else None
            create_task(name, description)
        elif sys.argv[1] == "delete":
            delete_task(sys.argv[2])
        elif sys.argv[1] == "schange":
            change_task_status(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "nchange":
            change_task_name(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "filter":
            filter_tasks(sys.argv[2])
        elif sys.argv[1] == "help":
            show_help()
        else:
            print(f"\nThere's not such a command.")
            show_help()
    except IndexError:
        print("Write a command after 'py main.py'")
        show_help()