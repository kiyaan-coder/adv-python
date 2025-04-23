# Simple TODO Application

def display_menu():
    print("\nTODO Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting TODO Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()