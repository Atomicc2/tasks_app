import sqlite3 as sql


#Função simples pra fazer a conexão com o db e criar o cursor
def connect_db():
    con = sql.connect('tasks_manager.db')
    cursor = con.cursor()
    return con, cursor

#Função simples para dar o commit e fechar a conexão com o db
def close_db(con):
    con.commit()
    con.close()

#Função para criar o banco de dados e as tabelas nele contidas
def create_db():
    con, cursor = connect_db()

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

    close_db(con)

#Função para adiconar um novo usuário, ou seja, cadastro
def add_user(username, password):
    con, cursor = connect_db()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        print('User registered successfully!')
    except sql.IntegrityError:
        print('Username already exists!')
    
    close_db(con)

#Checa se o usuário existe
def autenticate_user(username, password):
    con, cursor = connect_db()

    cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    close_db(con)
    return user is not None


