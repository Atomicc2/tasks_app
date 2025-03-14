import tkinter as tk
from tkinter import messagebox


#Função que cria a tela de login para autenticação
def login_screen(database):
    #Cria a tela com o nome em cima e o tamanho dela
    window = tk.Tk()
    window.title('Login')
    window.geometry('300x200')

    #Cria um texto com o nome Username e logo abaixo uma caixa para entrada de texto
    tk.Label(window, text='Username').pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    #Cria uma caixa de entrada para a senha e faz a proteção
    tk.Label(window, text='Password').pack()
    password_entry = tk.Entry(window, show='*')
    password_entry.pack()

    result = {'Success': False}
    user = {'Username': ''}

    #Confere se o usuário existe realmente
    def login_user():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        res = database.authenticate_user(username, password)
        if res:
            messagebox.showinfo('Success', f'Welcome, {username}!')
            result['Success'] = True
            user['Username'] = username
            window.destroy()
        else:
            messagebox.showerror('Erro', f'Username or Password incorrect!')

    #Cria o botão de faz o login e executa a função de login_user
    tk.Button(window, text='Login', command=login_user).pack()
    window.mainloop()
    return result['Success'], user['Username']