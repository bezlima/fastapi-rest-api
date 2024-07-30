# FASTAPI REST API


Este projeto é uma API REST desenvolvida com FastApi e Python, projetada para gerenciar usuários com funcionalidades básicas de autenticação e manipulação. A API oferece as seguintes características:

- Cadastro de Usuário: Permite criar novos usuários fornecendo informações como nome de usuário, email e senha.

- Login com JWT: Utiliza JSON Web Tokens (JWT) para autenticação. Usuários podem se autenticar e receber um token JWT para acessar rotas protegidas.

Manipulação de Usuários:

- Ver Todos: Recupera uma lista de todos os usuários registrados.

- Ver Um: Recupera os detalhes de um usuário específico com base em seu ID.

- Deletar Um: Permite excluir um usuário específico pelo seu ID.

A API é projetada para ser simples, com foco na gestão de usuários e autenticação.

## Autor
#### Lucas Lima  - *Desenvolvedor web*

[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bezlima)

[![linkedin](https://img.shields.io/badge/linkedin-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bezlima/)

[![portfolio](https://img.shields.io/badge/portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://bezlima-portfolio.vercel.app/)

## Rodando localmente

Em seu terminal:

Clone o projeto

```bash
  git clone https://github.com/bezlima/fastapi-rest-api.git
```

Entre no diretório do projeto

```bash
  cd fastapi-rest-api
```
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente na raiz do seu projeto.

#### `.env`

```toml
SECRET_KEY = "String" 
ALGORITHM = "String"
SQLALCHEMY_DATABASE_URL = "String"
```

## Instalação

Em seu terminal:

Crie um ambiente de virtual

```bash
python -m venv .venv
```

Verifique o ambiente

```bash
which python
```

Ative o ambeiente

```bash
source .venv/bin/activate
```

Instale o gerenciador de dependencias

```bash
pip install poetry
```

Instale as dependencias

```bash
poetry install
```

Rode o projeto

```bash
uvicorn app.main:app --reload
```

Finalizando o ambiente

```bash
deactivate
```
## Documentação da API

#### Retorna um ambiente para testar as rotas

```http
  GET /docs
```

## Dependencies
pip install fastapi
pip install sqlalchemy
pip install bcrypt
pip install python-jose
pip install pyjwt
pip install python-dotenv