import time
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "data", "tasks.json")

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
        print("Succesfully!")

def print_task(task): #Done
    print(f"ID: {task["ID"]}")
    print(f"Name: {task["Name"]}")
    print(f"Status: {task["Status"]}")
    print(f"Date: {task["Date"]}")
    print(f"Last change: {task["Last Change"]}")

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
        print("-" * 20)
        
def create_task(): #Done
    json_file = open_json()
    task_name = input("> ")
    task_creating_time = time.strftime("%d/%m/%y %H:%M:%S")
    task_id = json_file["LAST ID"] + 1
    json_file["TASKS"].append({
                       "ID": task_id,
                       "Name": task_name,
                       "Status": "Created",
                       "Date": task_creating_time,
                       "Last Change": task_creating_time
    })
    json_file["LAST ID"] += 1
    save_json(json_file)

def delete_task():
    pass

def change_task_status():
    pass

def change_task_name():
    pass

def filter_tasks():
    pass

create_task()
create_task()
create_task()
list_tasks()