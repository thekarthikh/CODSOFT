import tkinter as tk

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_list = tk.Listbox(self.root)
        self.task_list.pack()

        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.mark_complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Add more widgets and functionalities

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.task_list.insert(tk.END, task_description)
            self.task_entry.delete(0, tk.END)

    def mark_complete(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.itemconfig(selected_index, {'bg': 'green'})

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()