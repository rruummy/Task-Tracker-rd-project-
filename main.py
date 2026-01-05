# Main file
# Перевірка на наявність .json
# Загружаємо файл
# Очікуємо команди

import time
import json
import os

statuses = ('Created', 'In progress', 'Done')
def create_task(): # Зроблено
    with open(r"data/tasks.json", "r") as task_list:
        task_list = json.load(task_list)
    task_name = input("Enter a title of task: ")
    task_creating_time = time.strftime("%d/%m/%y %H:%M:%S")
    task_id = len(task_list)
    for task_names in task_list:
        if task_list[task_names]["id"] == task_id:
            task_id += 1
    print(task_id)
    task_list[task_name] = {
                        "id": task_id,
                        "status": 'Created',
                        "date": task_creating_time,
                        "done_time": None
    }
    with open(r'data/tasks.json', 'w+') as json_file:
        json.dump(task_list, json_file, indent=4)
    print(f'The task "{task_name}" successfully has been created!\n')

def delete_task(): # Зроблено
    with open(r"data/tasks.json", "r") as task_list:
        task_list = json.load(task_list)
    del_id = int(input("Enter id of task, which would you like to delete: "))
    print('Searching...')
    for task_names in task_list:
        if task_list[task_names]["id"] == del_id:
            print(f'The task "{task_names}" has been succesfully deleted!\n')
            del task_list[task_names]
            break
    else:
        print(f'Task with {del_id} id has not been found...\n')
    with open(r'data/tasks.json', 'w+') as json_file:
        json.dump(task_list, json_file, indent=4)

def change_status(): # Зроблено
     with open(r"data/tasks.json", "r") as task_list:
        task_list = json.load(task_list)
        chosen_id = int(input("Enter id of task, which would you like to edit: "))
        chosen_status = input("Enter status of task(In progress/Done): ")
        if chosen_status in statuses:
            print('Searching...')
            for task_names in task_list:
                if task_list[task_names]["id"] == chosen_id:
                    print(f'The task "{task_names}" status has been succesfully changed!\n')
                    task_list[task_names]["status"] = chosen_status
                    break
            else:
                print(f'Task with {chosen_id} id has not been found...\n')
            with open(r'data/tasks.json', 'w+') as json_file:
                json.dump(task_list, json_file, indent=4)
        else:
            print(f"You write a wrong status! '{chosen_status}' You can choose 'Created', 'In progress', 'Done'.")

def show_tasks(): #Зроблено
    print("Reading a file...")
    with open(r"data/tasks.json", "r") as task_list:
        task_list = json.load(task_list)
    mode = input("Enter a mode(All, Created, In progress, Done) to show: ")
    if mode == 'All':
        print('-'*20)
        for task_names in task_list:
            print(f'Title: {task_names}')
            print(f'Id: {task_list[task_names]["id"]}')
            print(f'Status: {task_list[task_names]["status"]}')
            print(f'Creating time: {task_list[task_names]["date"]}')
            print(f'Done time: {task_list[task_names]["done_time"]}')
            print('-'*20)
    elif mode == 'Created':
        print('-'*20)
        for task_names in task_list:
            if task_list[task_names]["status"] == 'Created':
                print(f'Title: {task_names}')
                print(f'Id: {task_list[task_names]["id"]}')
                print(f'Status: {task_list[task_names]["status"]}')
                print(f'Creating time: {task_list[task_names]["date"]}')
                print(f'Done time: {task_list[task_names]["done_time"]}')
                print('-'*20)
    elif mode == 'In progress':
        print('-'*20)
        for task_names in task_list:
            if task_list[task_names]["status"] == 'In progress':
                print(f'Title: {task_names}')
                print(f'Id: {task_list[task_names]["id"]}')
                print(f'Status: {task_list[task_names]["status"]}')
                print(f'Creating time: {task_list[task_names]["date"]}')
                print(f'Done time: {task_list[task_names]["done_time"]}')
                print('-'*20)
    elif mode == 'Done':
        print('-'*20)
        for task_names in task_list:
            if task_list[task_names]["status"] == 'Done':
                print(f'Title: {task_names}')
                print(f'Id: {task_list[task_names]["id"]}')
                print(f'Status: {task_list[task_names]["status"]}')
                print(f'Creating time: {task_list[task_names]["date"]}')
                print(f'Done time: {task_list[task_names]["done_time"]}')
                print('-'*20)
    else:
        print("There is such a type of mode!")
    
