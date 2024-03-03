import os
import json
import datetime

class Task:
    def __init__(self, title, priority, due_date):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        return f"{self.title} ({self.priority}) - Due: {self.due_date}"

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                tasks = json.load(file)
                return [Task(**task) for task in tasks]
        else:
            return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def add_task(self, title, priority, due_date):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    def mark_completed(self, index):
        self.tasks[index].completed = True
        self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

def main():
    task_manager = TaskManager('tasks.json')

    while True:
        print("\nTo-Do List Application")
        print("1: Add Task")
        print("2: Remove Task")
        print("3: Mark Completed")
        print("4: List Tasks")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(title, priority, due_date)
        elif choice == '2':
            index = int(input("Enter task index to remove: "))
            task_manager.remove_task(index)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            task_manager.mark_completed(index)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()