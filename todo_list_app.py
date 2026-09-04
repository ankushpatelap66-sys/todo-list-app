"""
To-Do List App
---------------
A simple command-line to-do list that lets the user add, view,
and remove tasks. Tasks are saved to a text file so they are
not lost when the program closes.
"""

FILE_NAME = "tasks.txt"


def load_tasks():
    """Read tasks from the file into a list."""
    try:
        with open(FILE_NAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Write the current list of tasks back to the file."""
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def view_tasks(tasks):
    print("\n----- Your Tasks -----")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("-----------------------")


def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    print("===== To-Do List App =====")

    while True:
        print("\n1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
