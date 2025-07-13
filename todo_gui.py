import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

# 🔁 Ensure task format is always a dict with 'due'
for i, t in enumerate(tasks):
    if isinstance(t, str):
        tasks[i] = {"task": t, "completed": False, "due": ""}
    elif "due" not in t:
        tasks[i]["due"] = ""

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        due = f" - Due: {task['due']}" if task["due"] else ""
        listbox.insert(tk.END, f"{task['task']} [{status}]{due}")

def add_task():
    task_text = entry.get()
    due_text = due_entry.get()
    if not task_text.strip():
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
    tasks.append({"task": task_text, "completed": False, "due": due_text})
    save_tasks()
    entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    refresh_list()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Info", "No task selected.")
        return
    tasks.pop(selected[0])
    save_tasks()
    refresh_list()

def mark_completed():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Info", "No task selected.")
        return
    tasks[selected[0]]["completed"] = True
    save_tasks()
    refresh_list()

def edit_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showinfo("Info", "No task selected.")
        return
    index = selected[0]
    new_task = entry.get()
    new_due = due_entry.get()
    if not new_task.strip():
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
    tasks[index]["task"] = new_task
    tasks[index]["due"] = new_due
    save_tasks()
    refresh_list()
    entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)

# 🖼️ GUI setup
root = tk.Tk()
root.title("To-Do List GUI with Due Dates")

tk.Label(root, text="Task:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Due Date:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
due_entry = tk.Entry(root, width=40)
due_entry.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Add Task", width=12, command=add_task)
btn_add.grid(row=0, column=2, padx=5)

btn_edit = tk.Button(root, text="Edit Task", width=12, command=edit_task)
btn_edit.grid(row=1, column=2, padx=5)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=2, column=0, columnspan=3, padx=10)

btn_delete = tk.Button(root, text="Delete Task", width=12, command=delete_task)
btn_delete.grid(row=3, column=0, pady=10)

btn_complete = tk.Button(root, text="Mark Completed", width=12, command=mark_completed)
btn_complete.grid(row=3, column=2, pady=10)

refresh_list()
root.mainloop()
