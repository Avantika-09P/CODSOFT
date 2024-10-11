import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        # Task storage
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        # Task input frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)

        # Task Label and Entry
        self.task_label = tk.Label(input_frame, text="Enter Task:", font=("Arial", 12), bg="#f0f0f0")
        self.task_label.grid(row=0, column=0, padx=10, pady=5)
        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=1, padx=10, pady=5)

        # Time Label and Entry (for timestamp)
        self.time_label = tk.Label(input_frame, text="Due Time (HH:MM):", font=("Arial", 12), bg="#f0f0f0")
        self.time_label.grid(row=1, column=0, padx=10, pady=5)
        self.time_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
        self.time_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Add Task Button
        self.add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=0, padx=10)

        # Remove Task Button
        self.remove_button = tk.Button(button_frame, text="Remove Task", font=("Arial", 12), command=self.remove_task, bg="#F44336", fg="white")
        self.remove_button.grid(row=0, column=1, padx=10)

        # Update Task Button
        self.update_button = tk.Button(button_frame, text="Update Task", font=("Arial", 12), command=self.update_task, bg="#FFC107", fg="white")
        self.update_button.grid(row=0, column=2, padx=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=10, width=50, font=("Arial", 12), bg="#fff", fg="#333", selectbackground="#ADD8E6")
        self.task_listbox.pack(pady=20)

        # Scrollbar for the Listbox
        self.scrollbar = ttk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.task_entry.get()
        due_time = self.time_entry.get()
        if task and due_time:
            # Combine task and due time
            try:
                # Validate time format
                datetime.datetime.strptime(due_time, "%H:%M")
                task_with_time = f"{task} (Due: {due_time})"
                self.tasks.append((task, due_time))
                self.task_listbox.insert(tk.END, task_with_time)
                self.task_entry.delete(0, tk.END)
                self.time_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter time in HH:MM format.")
        else:
            messagebox.showwarning("Input Error", "Please enter both task and due time.")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Task Removed", "Task removed successfully.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.task_entry.get()
            due_time = self.time_entry.get()
            if task and due_time:
                # Validate time format
                try:
                    datetime.datetime.strptime(due_time, "%H:%M")
                    task_with_time = f"{task} (Due: {due_time})"
                    self.tasks[task_index] = (task, due_time)
                    self.task_listbox.delete(task_index)
                    self.task_listbox.insert(task_index, task_with_time)
                    self.task_entry.delete(0, tk.END)
                    self.time_entry.delete(0, tk.END)
                    messagebox.showinfo("Task Updated", "Task updated successfully.")
                except ValueError:
                    messagebox.showwarning("Input Error", "Please enter time in HH:MM format.")
            else:
                messagebox.showwarning("Input Error", "Please enter both task and due time.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

