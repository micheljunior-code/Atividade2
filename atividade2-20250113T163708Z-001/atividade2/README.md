Gerenciador de Tarefas com FastAPI e SQLite
Este projeto utiliza FastAPI e SQLite para gerenciar tarefas. O SQLite é um banco de dados leve e fácil de usar, ideal para armazenar dados localmente.

Banco de Dados
Como Funciona
O banco de dados usado é o SQLite .
Ele armazena as tarefas em um arquivo chamado tarefas.db, criado automaticamente ao rodar o projeto.
Estrutura do Banco
A tabela principal é tarefas, que contém:

id : Identificador de tarefa.
título : Nome da tarefa.
descricao : Detalhes da tarefa.
completa : Indica se a tarefa foi concluída.
Como usar
Rodar o Projeto : Execute o comando abaixo para iniciar o projeto e criar o banco de dados automaticamente:

bater

Copiar código
uvicorn main:app --reload
Dados Manipulares : Use as rotas da API para adicionar, visualizar, atualizar ou excluir tarefas.

Rotas Principais
Criar Tarefa :POST /tarefas/
Ler Tarefa :GET /tarefas/{id}
Atualizar Tarefa :PUT /tarefas/{id}
Excluir Tarefa :DELETE /tarefas/{id}
Este guia fornece tudo o que você precisa para começar a usar o banco de dados no projeto de Gerenciador de Tarefas.