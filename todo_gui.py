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

# Ensure all tasks are in dict format
for i, t in enumerate(tasks):
    if isinstance(t, str):
        tasks[i] = {"task": t, "completed": False}

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{task['task']} [{status}]")

def add_task():
    task_text = entry.get()
    if not task_text.strip():
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
    tasks.append({"task": task_text, "completed": False})
    save_tasks()
    entry.delete(0, tk.END)
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

# Setup GUI
root = tk.Tk()
root.title("To-Do List GUI")

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

btn_add = tk.Button(root, text="Add Task", width=12, command=add_task)
btn_add.grid(row=0, column=1)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=1, column=0, columnspan=2, padx=10)

btn_delete = tk.Button(root, text="Delete Task", width=12, command=delete_task)
btn_delete.grid(row=2, column=0, pady=10)

btn_complete = tk.Button(root, text="Mark Completed", width=12, command=mark_completed)
btn_complete.grid(row=2, column=1)

refresh_list()
root.mainloop()
