import sqlite3 as sql


#Classe para armazenas as funções da base de dados
class Database:

    def __init__(self, name_db='tasks_manager.db'):
        self.name_db = name_db

    #Função simples pra fazer a conexão com o db e criar o cursor
    def connect_db(self):
        con = sql.connect(self.name_db)
        cursor = con.cursor()
        return con, cursor

    #Função simples para dar o commit e fechar a conexão com o db
    def close_db(self, con):
        con.commit()
        con.close()

    #Função para criar o banco de dados e as tabelas nele contidas
    def create_db(self):
        con, cursor = self.connect_db()

        #Criando a tabela com as informações dos usuários
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(                           
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        ''')

        #Criando a tabela das tasks
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )               
        ''')

        self.close_db(con)

    #Função para adiconar um novo usuário, ou seja, cadastro
    def add_user(self, username, password):
        con, cursor = self.connect_db()

        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.close_db()
        except sql.DatabaseError as error:
            self.close_db()
            raise error
        
    #Checa se o username já existe
    def check_user(self, username):
        con, cursor = self.connect_db()

        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        self.close_db(con)
        return user is not None

    #Checa se o usuário já está cadastrado
    def authenticate_user(self, username, password):
        con, cursor = self.connect_db()

        cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        self.close_db(con)
        return user is not None



