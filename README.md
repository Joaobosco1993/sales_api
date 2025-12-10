# Sales API (FastAPI + SQLModel + MySQL)

Projeto exemplo pronto para deploy local / server Ubuntu.

## O que tem
- CRUD de produtos
- Autenticação JWT (signup/login)
- Endpoints para criar pedidos
- Docker + Docker Compose (MySQL + app)
- Testes com pytest
- README com exemplos de requests

## Rodando com Docker Compose (recomendado)
1. Ajuste `.env` se necessário.
2. `docker-compose up --build`
3. Acesse docs: http://localhost:8000/docs

## Rodando sem Docker (rápido, usando SQLite para testes)
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. export DATABASE_URL=sqlite:///./test.db
5. uvicorn app.main:app --reload

## Testes (usando SQLite local)
1. export DATABASE_URL=sqlite:///./test.db
2. pytest -q

## Testes manuais (curl)
# Signup
curl -X POST "http://localhost:8000/signup" -H "Content-Type: application/json" -d '{"username":"me","password":"secret"}'
# Get token
curl -X POST "http://localhost:8000/token" -d "username=me&password=secret"
# Create product (use token from previous step)
curl -X POST "http://localhost:8000/products" -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" -d '{"name":"Caneca","description":"Caneca legal","price":25.0,"stock":10}'

API de Vendas (FastAPI + SQLModel + MySQL)

Projeto completo de backend para gestão de vendas, desenvolvido com FastAPI, SQLModel e banco MySQL, seguindo boas práticas, arquitetura modular, autenticação JWT, testes automatizados e containerização com Docker.

🚀 Tecnologias Utilizadas

FastAPI

SQLModel

MySQL

Docker + Docker Compose

PyJWT

Passlib

Pydantic

Uvicorn

PyTest (testes unitários)

📌 Funcionalidades da API
🔐 Autenticação

Login com JWT

Criação de usuários

Proteção de rotas privadas

🛒 Módulos de Vendas

CRUD de produtos

CRUD de clientes

CRUD de vendas

Cálculo automático de total da venda

Associação produto ↔ venda

Relacionamentos usando SQLModel

🧪 Testes

Testes automatizados do CRUD de produtos

Fácil expansão para demais módulos
sales_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── deps.py
│   ├── auth.py
│   ├── crud.py
│   ├── routes/
│   │   ├── products.py
│   │   ├── users.py
│   │   └── sales.py
│   └── tests/
│       └── test_products.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
🐳 Rodando o projeto com Docker
1. Subir os containers
docker-compose up -d

2. Acessar a API
http://localhost:8000

3. Documentação automática (Swagger)
http://localhost:8000/docs

🛢️ Configuração do Banco MySQL

O banco MySQL sobe automaticamente pelo Docker usando:

Host: mysql

Porta: 3306

Usuário: root

Senha: password

Banco: salesdb

🔧 Rodar localmente sem Docker
1️⃣ Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar a aplicação
uvicorn app.main:app --reload

🧪 Rodar os testes
pytest
👨‍💻 Autor

João Bosco Ferreira
📧 joao_bosco93@hotmail.com

GitHub: https://github.com/Joaobosco1993

📄 Licença

Este projeto está sob a licença MIT.
