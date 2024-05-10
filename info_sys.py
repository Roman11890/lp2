class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")
    def view_tasks(self):
        if self.tasks:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("You have no tasks!")
def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
       ## print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            manager.remove_task(task)
        elif choice == '3':
            manager.view_tasks()
       ## elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
if __name__ == "__main__":
    main()
