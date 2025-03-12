# Esquema do Projeto: Lista de Tarefas com Cadastro e Login

## 1. Requisitos principais

### Cadastro de Usuário
- O usuário deve se cadastrar com um nome de usuário e senha.
- As credenciais de login serão armazenadas no banco de dados SQLite.

### Login
- O sistema deve permitir que o usuário entre com suas credenciais.

### Lista de Tarefas
- O usuário poderá adicionar, editar, excluir e marcar tarefas como concluídas.

### Interface Gráfica
- Usar **Tkinter** para a interface simples com abas.

### Banco de Dados
- Usar **SQLite** para armazenar os dados dos usuários e tarefas.
- **Usuários**: Tabela com id, username, password.
- **Tarefas**: Tabela com id, task, status, user_id.

## 2. Fluxo do projeto

### Tela de Cadastro
1. Entrada de dados: `username` e `password`.
2. Verificar se o nome de usuário já existe no banco de dados.
3. Se o nome de usuário for único, adicionar o novo usuário ao banco de dados.
4. Se já existir, exibir uma mensagem de erro.

### Tela de Login
1. Entrada de dados: `username` e `password`.
2. Verificar as credenciais no banco de dados.
3. Se o login for bem-sucedido, redireciona para a lista de tarefas.
4. Se o login falhar, exibe uma mensagem de erro.

### Tela de Lista de Tarefas
1. Exibir uma lista de tarefas associadas ao usuário logado.
2. Opções para:
   - Adicionar nova tarefa.
   - Editar (alterar descrição da tarefa).
   - Excluir (remover a tarefa).
   - Marcar como concluída (atualiza o status da tarefa no banco de dados).

## 3. Tecnologias e Ferramentas
- **Python** (para a lógica do backend).
- **Tkinter** (para a interface gráfica).
- **SQLite** (para o banco de dados).

## 4. Estrutura do Projeto
- `app.py` - arquivo principal que inicia a aplicação.
- `database.py` - responsável pela criação e manipulação do banco de dados SQLite.
- `ui.py` - interface gráfica com o Tkinter.
- `models.py` - definir classes de Usuário e Tarefa, opcional para organizar o código.

## 5. Passos para Desenvolvimento

### Configuração do Banco de Dados
1. Criar as tabelas `users` e `tasks` no SQLite.
2. Funções para adicionar, verificar e autenticar usuários.

### Tela de Cadastro
1. Criar a interface com campos para `username` e `password`.
2. Função para verificar se o `username` já existe.
3. Se não existir, salvar o novo usuário no banco de dados.

### Tela de Login
1. Criar a interface para entrada de `username` e `password`.
2. Função para validar o login, verificando as credenciais no banco.

### Tela de Lista de Tarefas
1. Criar a interface para listar as tarefas do usuário.
2. Funções para adicionar, editar, excluir e marcar tarefas como concluídas.

### Conectar tudo
1. Integrar as telas de cadastro, login e lista de tarefas, garantindo que o usuário passe pelo cadastro primeiro, depois faça o login e, finalmente, acesse a lista de tarefas.

## 6. Pontos de Atenção
- **Segurança**: Armazenar senhas de forma segura (usar hash em vez de texto simples).
- **Usabilidade**: Interface simples e intuitiva.
- **Manutenção**: Organizar o código para fácil manutenção, separando a lógica de banco de dados e interface.
