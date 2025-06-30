import getpass
from tabulate import tabulate
from typing import List, Dict
import os
from datetime import datetime
import humanize

VALID_USERS = {'miraj': "1234"}

username = str(input('Enter your username :'))
password = getpass.getpass('Password : ')

todos: List[Dict[str, object]] = []
# Add Todo


def addTodo(inputs: List):
    main_command = inputs[0]
    inputs.remove(main_command)  # removing the command a
    print('main-command', inputs)
    todo_text = " ".join(inputs)
    print(todo_text)
    if todo_text:
        newTodo = {
            "id": len(todos)+1,
            "name": todo_text,
            "done": False,
            'created_at': datetime.now()
        }
        todos.append(newTodo)
    else:
        print('Invalid todo')


def del_todo(id: int):
    global todos
    todo = next((item for item in todos if item['id'] == id), None)
    if todo:
        todos = [todo for todo in todos if todo["id"] != id]
        print(f"Deleted todo of {id}")
    else:
        print('Task not found')


# Mark todo as done
def mark_todo_done(id: int):
    todo = next((item for item in todos if item['id'] == id), None)
    if todo:
        todo["done"] = True
        print(f"{todo['name']} made done!")
    else:
        print('Task not found')


def show_all_todos():
    headers = ['ID', 'NAME', 'STATUS', 'CREATED_AT']
    formatted_todos = [
        [todo["id"], todo["name"], "✅" if todo["done"] else "❌",
         humanize.naturaltime(datetime.now() - todo["created_at"])]
        for todo in todos
    ]
    print(tabulate(formatted_todos, headers=headers, tablefmt='fancy_grid'))

# Show help Text


def help_instruction():
    help_text = """
        📘  Welcome to the Todo CLI Help Menu
        ----------------------------------------
        Commands:

        🔹 add <task description>
            Add a new task to your todo list.
            Example:
                add Buy groceries

        🔹 ls
            Show all tasks in a table.
            Displays ID, Task Name, and Status (✅ / ❌)

        🔹 done <task_id>
            Mark a task as completed.
            Example:
                done 2

        🔹 del <task_id>
            Delete a task by its ID.
            Example:
                del 3

        🔹 help
            Show this help message.

        🔹 exit 
            Exit the application.

        📌 Notes:
        - Task IDs are shown in the first column of the `ls` command.
        - You must use the numeric ID when marking as done or deleting.
        - Quotation marks are optional unless your task contains multiple words.

        Enjoy being productive! ✅
        """
    print(help_text)

# Clear console


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if username in VALID_USERS and password == VALID_USERS[username]:
    print('Login Successfully\n')
    while True:
        command = input('todo> ').strip()

        inputs = command.split(" ")  # spliting for geting the command first

        if command == 'help':
            help_instruction()

        if command == 'clear':
            clear_console()

        if inputs[0] == 'del':
            id = int(inputs[1])
            PermissionError(id)
            del_todo(id)

        if command == 'ls':
            show_all_todos()

        if inputs[0] == 'done':
            id = int(inputs[1])
            mark_todo_done(id)

        if command == 'exit':
            break

        if inputs[0] == 'add':
            addTodo(inputs)


else:
    print('Invalid Credentials')
    exit()


# Delete todo

# Show todo

# Help /to show all the commands
