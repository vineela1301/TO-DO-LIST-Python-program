import os

class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Incomplete"})
        print(f"Task '{task}' added!")
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task['task']} - {task['status']}")
    
    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task '{removed['task']}' removed!")
        else:
            print("Invalid task number.")
    
    def update_task(self, task_number, new_task=None, new_status=None):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if new_task:
                task["task"] = new_task
            if new_status:
                task["status"] = new_status
            print(f"Task {task_number} updated!")
        else:
            print("Invalid task number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Exit")

def main():
    app = TodoApp()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task description: ")
            app.add_task(task)
        elif choice == "2":
            app.list_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to remove: "))
            app.remove_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task description (leave blank to keep current): ")
            new_status = input("Enter the new status (Incomplete/Complete, leave blank to keep current): ")
            app.update_task(task_number, new_task or None, new_status or None)
        elif choice == "5":
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
