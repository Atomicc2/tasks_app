from ui.login import login_screen
from ui.register import register_screen
from ui.tasks import tasks_screen
import tkinter as tk

#Função que cria a janela inicial do programa
def main_screen(db):
    window = tk.Tk()
    window.title('Task Manager')
    window.geometry('300x200')

    tk.Label(window, text='Welcome to your personal Task Manager!').pack()

    #Acão caso a forma de entrar escolhida seja o login
    def login_action():
        window.destroy()
        res, username = login_screen(db)
        if res:
            tasks_screen(db, username)

    #Ação caso a forma de entrar escolhida seja o registro
    def register_action():
        window.destroy()
        res, username = register_screen(db)
        if res:
            tasks_screen(db, username)

    tk.Button(window, text='Login', command=login_action).pack()
    tk.Button(window, text='Register', command=register_action).pack()

    window.mainloop()
