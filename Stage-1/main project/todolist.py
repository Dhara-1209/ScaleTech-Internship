import os
import csv

filename = "tasks.csv"
tasks = []


def load_task():
    global tasks

    tasks = []

    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                tasks.append({
                    "task": row["task"],
                    "completed": row["completed"] == "True"
                })


def add_tasks():
    task = input("Enter a task: ").strip()

    if task:
        tasks.append({
            "task": task,
            "completed": False
        })
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def visit_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\n***** Tasks *****")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")


def delete_tasks():
    visit_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted: {removed_task['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_tasks():
    visit_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def save_tasks():
    with open(filename, "w", newline="") as file:
        fieldnames = ["task", "completed"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)


def main():
    load_task()

    menu = """
*****   To-Do List   ******

1. View Tasks
2. Add Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
"""

    while True:
        print(menu)

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                visit_tasks()

            elif choice == 2:
                add_tasks()

            elif choice == 3:
                complete_tasks()

            elif choice == 4:
                delete_tasks()

            elif choice == 5:
                save_tasks()
                print("Tasks saved.")
                print("Goodbye!!")
                break

            else:
                print("Invalid option. Please choose between 1 to 5.")

        except ValueError:
            print("Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()