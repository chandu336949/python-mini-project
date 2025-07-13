import json
import os

FILE_NAME = "tasks.json"

# ---------- Load & auto‑upgrade ----------
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

# 🔧 Convert any legacy string entries → dict format
for i, t in enumerate(tasks):
    if isinstance(t, str):
        tasks[i] = {"task": t, "completed": False}

def save_tasks() -> None:
    """Write current task list to tasks.json"""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu() -> None:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

# -------------- Main loop --------------
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":            # Add
        task_text = input("Enter the task: ")
        tasks.append({"task": task_text, "completed": False})
        save_tasks()
        print("✅ Task added!")

    elif choice == "2":          # View
        print("\n📝 Your Tasks:")
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "3":          # Delete
        if not tasks:
            print("No tasks to delete.")
            continue
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks()
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("Invalid task number.")

    elif choice == "4":          # Mark completed
        if not tasks:
            print("No tasks to mark as completed.")
            continue
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            save_tasks()
            print(f"✔ Task marked as completed: {tasks[index - 1]['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":          # Exit
        print("👋 Goodbye!")
        break

    else:
        print("❗ Invalid choice. Please select a number from 1 to 5.")


