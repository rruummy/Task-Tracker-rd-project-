
```markdown
# CLI Task Manager (Python)
----------------------------------------
https://roadmap.sh/projects/task-tracker
A simple console-based Task Manager written in **Python**.
The application allows you to create, view, update, delete, and filter tasks
stored in a local **JSON file**.

This project was created for educational purposes and can be used as
a coursework, practice project, or a junior developer portfolio example.
----------------------------------------

## Features
----------------------------------------
[+] Create new tasks  
[*] View all tasks  
[~] Change task status  
[>] Change task name  
[-] Delete tasks  
[?] Filter tasks by status  
[!] Input validation and error handling  

----------------------------------------

## Project Structure
----------------------------------------
```

project/
│
├── main.py
├── data/
│   └── tasks.json
└── README.md

````

- `main.py`   : main application file  
- `tasks.json`: JSON storage for tasks (created automatically)

----------------------------------------

## Task Data Structure
----------------------------------------
Each task is stored in the following format:

```json
{
    "ID": 1,
    "Name": "Example task",
    "Description": "Task description",
    "Status": "Created",
    "Date": "20/01/26 23:05:36",
    "Last Change": "20/01/26 23:05:36"
}
````

### Available statuses:

* `Created`
* `In progress`
* `Done`

---

## Requirements

---

* Python 3.8 or higher
* No external libraries required

---

## How to Run

---

Use the command line:

```bash
python main.py <command> [arguments]
```

---

## Available Commands

---

### Show all tasks

```bash
python main.py list
```

### Create a new task

```bash
python main.py create "Task name" "Task description"
```

### Delete a task by ID

```bash
python main.py delete 1
```

### Change task status

```bash
python main.py schange 1 "In progress"
```

### Change task name

```bash
python main.py nchange 1 "New task name"
```

### Filter tasks by status

```bash
python main.py filter "Done"
```

### Show help

```bash
python main.py help
```

---

## Error Handling

---

The program safely handles:

* Invalid or missing command-line arguments
* Non-numeric task IDs
* Non-existent tasks
* Invalid task statuses

---

## Technologies Used

---

* Python 3
* JSON file storage
* Standard library modules:

  * os
  * sys
  * json
  * time

---