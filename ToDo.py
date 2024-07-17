import os

# Define the file to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index] += " [Completed]"
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
