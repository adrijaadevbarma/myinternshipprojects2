import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create and configure the task list
        self.task_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_list.pack(pady=10)

        # Create task entry fields
        self.description_entry = tk.Entry(self.root, width=50)
        self.description_entry.pack()
        self.due_date_entry = tk.Entry(self.root, width=50)
        self.due_date_entry.pack()
        self.priority_entry = tk.Entry(self.root, width=50)
        self.priority_entry.pack()

        # Create buttons for actions
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)
        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.complete_task)
        self.complete_button.pack()
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack()
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        # Populate the task list
        self.populate_task_list()

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if description:
            task = (description, due_date, priority, False)
            self.tasks.append(task)
            self.populate_task_list()
            self.clear_entry_fields()
        else:
            messagebox.showerror("Error", "Please enter a task description.")

    def complete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks[index] = (task[0], task[1], task[2], True)
            self.populate_task_list()

    def update_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            description = self.description_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()
            task = self.tasks[index]
            self.tasks[index] = (description, due_date, priority, task[3])
            self.populate_task_list()
            self.clear_entry_fields()

    def remove_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.populate_task_list()

    def clear_entry_fields(self):
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def populate_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task[3] else " "
            self.task_list.insert(tk.END, f"{status} {task[0]}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
