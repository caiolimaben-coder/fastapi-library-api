# FastAPI Book API

API REST desenvolvida com FastAPI para gerenciamento de livros.

## Tecnologias

- Python
- FastAPI
- Pydantic

## Funcionalidades

- CRUD completo de livros (Create, Read, Update e Delete)
- Arquitetura organizada em módulos
- Validação de dados com Pydantic

## Estrutura do projeto

```
library-api/
│
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── livros.py
│   ├── main.py
│   ├── models.py
│   └── database.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Como executar

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```

Depois acesse:

```
http://127.0.0.1:8000/docs
```

## Próximos passos

- [ ] Integração com PostgreSQL
- [ ] SQLAlchemy
- [ ] Alembic
- [ ] Docker
- [ ] Autenticação JWT