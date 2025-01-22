import tkinter as tk  # GUI Import
from tkinter import messagebox, filedialog  # Benachrichtungsbox
import csv


class TodoApp:
    def __init__(self, root):
        self.root = root  # Hauptfenster was von tkinter bereitgestellt wird
        self.root.title("ToDo List")  # Überschrift
        self.tasks = []  # Liste der Todos
        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(
            self.root, text="Add Task", command=self.add_task
        )
        self.add_task_button.pack(pady=10)

        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(
            self.root, text="Delete Task", command=self.delete_task
        )
        self.delete_task_button.pack(pady=10)

        self.save_tasks_button = tk.Button(
            self.root, text="Save Tasks", command=self.save_tasks
        )
        self.save_tasks_button.pack(pady=10)

        self.load_tasks_button = tk.Button(
            self.root, text="Load Tasks", command=self.load_tasks
        )
        self.load_tasks_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must select a Task.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task])
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, mode="r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    self.tasks = [task[0] for task in reader]
                self.update_tasks_listbox()
                messagebox.showinfo("Info", "Tasks loaded successfully.")
            except FileNotFoundError:
                messagebox.showwarning("Warning", "No saved tasks found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
