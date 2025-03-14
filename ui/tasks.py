import tkinter as tk
from tkinter import messagebox
from database.db import Database


#Função que controla a tela de tarefas
def tasks_screen(database, username):
    window = tk.Tk()
    window.title('Tasks')
    window.geometry('600x400')

    tk.Label(window, text='Tasks').pack()
    tasks_listbox = tk.Listbox(window)
    tasks_listbox.pack()

    new_task_entry = tk.Entry(window)
    new_task_entry.pack()
    
    #Função para adicionar uma nova tarefa
    def add_new_task():
        new_task = new_task_entry.get()
        if new_task:
            res = database.add_tasks(new_task, username)
            if res:
                messagebox.showinfo('Success', 'New task added!')
                update_task_list()
            else:
                messagebox.showerror('Error', 'Impossible add new task')
        else:
            messagebox.showerror('Error', 'Type something!')

    #Função para exluir a tarefa selecionada pelo usuário
    def delete_task():
        try:
            selected_task_index = tasks_listbox.curselection()
            if not selected_task_index:
                raise IndexError
            
            selected_task = tasks_listbox.get(selected_task_index)
            res = database.del_tasks(selected_task, username)
            if res:
                messagebox.showinfo('Success', 'Task deleted')
                update_task_list()
            else:
                messagebox.showerror('Error', 'Task deletion failed')
        except IndexError:
            messagebox.showwarning('Warning', 'Please select  task to delete')

        
    #Função para atualizar o status da tarefa selecionada pra completa
    def complete_task():
        try:
            selected_task_index = tasks_listbox.curselection()
            if not selected_task_index:
                raise IndexError
            
            selected_task = tasks_listbox.get(selected_task_index)
            res = database.set_status_complete(selected_task, username)
            if res:
                messagebox.showinfo('Success', 'Task marked as complete!')
                update_task_list()
            else:
                messagebox.showerror('Error', 'Failed to update task status!')
        except IndexError:
            messagebox.showwarning('Warning', 'please select task to complete')

    #Função para atualizar a tela de tarefas
    def update_task_list():
        tasks_listbox.delete(0, tk.END)
        tasks = database.list_tasks(username)
        if tasks:
            for task in tasks:
                tasks_listbox.insert(tk.END, task[0])
        else:
            tasks_listbox.insert(tk.END, 'No tasks found')

    tk.Button(window, text='Add new task', command=add_new_task).pack()
    tk.Button(window, text='Delete task', command=delete_task).pack()
    tk.Button(window, text='Complete task', command=complete_task).pack()

    update_task_list()
    window.mainloop()