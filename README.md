Gerenciador de Tarefas com FastAPI e SQLite
Este projeto usa FastAPI e SQLite para gerenciar tarefas de forma simples e eficiente.

Banco de Dados
Configuração
O banco de dados utilizado é SQLite , que armazena os dados localmente no arquivo tarefas.db.
A configuração do banco de dados não é arquivo database.py.
Como Funciona
Criação Automática : O banco de dados tarefas.dbé criado automaticamente na primeira vez que você executa o projeto.
Interação com o Banco : Você pode interagir com o banco de dados através das rotas da API.
Rotas Principais
Criar Tarefa : POST /tarefas/— Adiciona uma nova tarefa.
Ler Tarefa : GET /tarefas/{tarefa_id}— Recuperar uma tarefa pelo ID.
Atualizar Tarefa : PUT /tarefas/{tarefa_id}— Atualiza uma tarefa existente.
Deletar Tarefa : DELETE /tarefas/{tarefa_id}— Remover uma tarefa.
Visualização do Banco de Dados
O arquivo tarefas.dbpode ser visualizado e editado usando ferramentas como DB Browser for SQLite .
