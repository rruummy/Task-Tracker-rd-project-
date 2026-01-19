import time
import json
import os
import sys

def open_json(): #Done
    if not os.path.exists(JSON_PATH):
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        with open(JSON_PATH, "w") as data:
            pattern = {"LAST ID": 0, "TASKS": []}
            json.dump(pattern, data, indent=4)
    with open(JSON_PATH, "r") as data:
            return json.load(data)

def save_json(json_file): #Done
    with open(JSON_PATH, "w") as data:
        json.dump(json_file, data, indent=4)

def print_task(task): #Done
    print(f"ID: {task["ID"]}")
    print(f"Name: {task["Name"]}")
    print(f"Description: {task["Description"]}")
    print(f"Status: {task["Status"]}")  
    print(f"Date: {task["Date"]}")
    print(f"Last change: {task["Last Change"]}")
    print("-" * 20)

def search_task(id): #Done
    tasks = open_json()
    for task in tasks["TASKS"]:
        if task["ID"] == id:
            return task

def list_tasks(): #Done
    tasks = open_json()
    print("-" * 20)
    for task in tasks["TASKS"]:
        print_task(task)
        
def create_task(): #Done
    json_file = open_json()
    task_name = input("> ")
    task_description = input("> ")
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
    save_json(json_file)

def delete_task(): # Done
    json_file = open_json()
    ch_id = int(input("> "))
    json_file["TASKS"].remove(search_task(ch_id)) # Delete a task
    save_json(json_file)

def change_task_status(): #Done
    json_file = open_json()
    ch_status = input("> ")
    if ch_status not in ('Created', 'In progress', 'Done'):
        return None
    ch_id = int(input("> "))
    for task in json_file["TASKS"]:
        if task["ID"] == ch_id:
            task_change_time = time.strftime("%d/%m/%y %H:%M:%S")
            task["Status"] = ch_status
            task["Last Change"] = task_change_time
    save_json(json_file)

def change_task_name(): #Done
    json_file = open_json()
    task_new_name = input("> ")
    ch_id = int(input("> "))
    for task in json_file["TASKS"]:
        if task["ID"] == ch_id:
            task_change_time = time.strftime("%d/%m/%y %H:%M:%S")
            task["Name"] = task_new_name
            task["Last Change"] = task_change_time
    save_json(json_file)

def filter_tasks(): #Done
    json_file = open_json()
    fil_status = input("> ")
    if fil_status not in ('Created', 'In progress', 'Done'):
        print("There`s not such status.(Write Created/In progress/Done)")
        return None
    print("-" * 20)
    [print_task(task) for task in json_file["TASKS"] if task["Status"] == fil_status]

def help():
    print("=" * 20)
    print("List of commands:")
    print("create - to create new task")
    print("delete - to delete task")
    print("list - show all tasks")
    print("schange - change a status of task")
    print("nchange - change a name of task")
    print("filter - show filtered tasks")
    print("=" * 20)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, "data", "tasks.json")
    if sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "create":
        create_task()
    elif sys.argv[1] == "delete":
        delete_task()
    elif sys.argv[1] == "schange":
        change_task_status()
    elif sys.argv[1] == "nchange":
        change_task_name()
    elif sys.argv[1] == "filter":
        filter_tasks()
    elif sys.argv[1] == "help":
        help()
    else:
        print(f"\nThere's not such a command.")
        help()