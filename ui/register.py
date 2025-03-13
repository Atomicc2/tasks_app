import tkinter as tk
from tkinter import messagebox


#Função para o registro de novos usuários
def register_screen(database):
    #Cria a tela de registro 
    window = tk.Tk()
    window.title('Register')
    window.geometry('300x200')

    #Cria a caixa de entrada para o username
    tk.Label(window, text='Username').pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    #Cria a caixa de entrada para o password
    tk.Label(window, text='Password').pack()
    password_entry = tk.Entry(window, show='*')
    password_entry.pack()

    #Função que realiza o cadastro no banco de dados
    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        #Confirma que os dois campos sejam preenchidos
        if username and password:
            res = database.check_user(username)
            #Condição para verificar se o nome de usuário já existe, caso exista, da erro
            if res:
                messagebox.showerror('ERRO', 'This username already exists!')
            else:
                database.add_user(username, password)
                messagebox.showinfo('Success', 'User registered!')
        else:
            messagebox.showerror('Error', 'Fill all fields')

    #Cria o botão para fazer o registro chamando a função register_user  
    tk.Button(window, text='Register', command=register_user).pack()
    window.mainloop()