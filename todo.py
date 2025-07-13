tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == '2':
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
    elif choice == '3':
        index = int(input("Enter task number to delete: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
            
    elif choice == '4':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice.")
