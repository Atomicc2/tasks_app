import tkinter as tk
from tkinter import messagebox


def tasks_screen(database):
    window = tk.Tk()
    window.title('Tasks')
    window.geometry('600x400')

    tk.Label(window, text='Tasks').pack()
    tasks_listbox = tk.Listbox(window)
    tasks_listbox.pack()

    new_task_entry = tk.Entry(window)
    new_task_entry.pack()
    
    def add_new_task():
        new_task = new_task_entry.get()
        res = database.add_tasks(new_task)
        if res:
            messagebox.showinfo('Success', 'New task added!')
            update_task_list()
        else:
            messagebox.showerror('Error', 'Impossible add new task')

    tk.Button(window, text='Add new task', command=add_new_task).pack()
    
    def update_task_list():
        tasks_listbox.delete(0, tk.END)
        tasks = database.list_tasks()
        for task in tasks:
            tasks_listbox.insert(tk.END, task[0])

    update_task_list()
    
    window.mainloop()