🛒 API de Vendas (FastAPI + SQLModel + MySQL)

Projeto backend completo para gestão de vendas, desenvolvido com FastAPI, SQLModel e MySQL, seguindo boas práticas, arquitetura modular, autenticação JWT, testes automatizados e containerização com Docker.

🚀 Tecnologias Utilizadas

FastAPI

SQLModel

MySQL

Docker + Docker Compose

PyJWT

Passlib

Pydantic

Uvicorn

PyTest (testes automatizados)

🔧 Funcionalidades da API
🔐 Autenticação

Login com JWT

Proteção de rotas privadas

Criação de usuários

🛍 Módulos de Vendas

CRUD de produtos

Endpoints para pedidos

Registro e controle de vendas

🐳 Rodando com Docker Compose (Recomendado)

Ajuste o arquivo .env se necessário

Execute:

docker-compose up --build


Acesse a documentação:
📄 http://localhost:8000/docs

⚡ Rodando sem Docker (SQLite para testes)
1️⃣ Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

2️⃣ Instalar dependências
pip install -r requisitos.txt

3️⃣ Rodar a aplicação
uvicorn app.main:app --reload

4️⃣ Rodar os testes
pytest

🗄 Banco MySQL (Docker)

O banco MySQL sobe automaticamente pelo Docker usando:

Host: mysql

Porta: 3306

Usuário: root

Senha: password

Banco: salesdb

👨‍💻 Autor

João Bosco Ferreira
📧 joao_bosco93@hotmail.com

🔗 GitHub: https://github.com/Joaobosco1993

📜 Licença

Este projeto está sob a licença MIT.
