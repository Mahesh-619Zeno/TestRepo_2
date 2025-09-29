import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as todo_file:
            return json.load(todo_file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def add_task(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})

def mark_done(todos):
    list_todos(todos)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
    else:
        print("Invalid index.")

def main():
    todos = load_todos()
    while True:
        print("\n1. List\n2. Add\n3. Mark Done\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_task(todos)
        elif choice == '3':
            mark_done(todos)
        elif choice == '4':
            save_todos(todos)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
