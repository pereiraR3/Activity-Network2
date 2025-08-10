# Activity-Network2

**Atividade 01 – Desafio com Containers**

Este projeto implementa uma solução computacional de 3 camadas utilizando Docker Compose, desenvolvido como resposta ao desafio proposto na disciplina de Redes de Computadores 2. A solução consiste em uma aplicação web Flask conectada a um banco de dados PostgreSQL, ambos executando em containers separados.

## Sobre a Atividade

A atividade consistiu em implementar uma solução computacional usando composição de containers com Docker Compose, seguindo uma arquitetura de 3 camadas:

- **Camada de Apresentação**: Navegador (Cliente)
- **Camada de Aplicação**: Servidor Web (Flask)
- **Camada de Dados**: SGBD (PostgreSQL)


## 📁 Estrutura do Projeto

```
Activity-Network2/
├── app/
│   └── app.py              # Aplicação Flask principal
├── docker-compose.yml      # Configuração dos containers
├── Dockerfile             # Build da aplicação
└── README.md              # Documentação
```

## Funcionalidades

- **Endpoint `/db_version`**: Retorna a versão do banco de dados PostgreSQL conectado
- **Conexão com PostgreSQL**: Estabelece conexão segura com o banco usando variáveis de ambiente
- **Containerização**: Aplicação completamente containerizada com Docker
- **Multi-container**: Separação clara entre aplicação e banco de dados

## 🛠️ Tecnologias Utilizadas

- **Python 3.10**: Linguagem de programação principal
- **Flask**: Framework web para Python
- **PostgreSQL**: Sistema de gerenciamento de banco de dados
- **Docker**: Containerização da aplicação
- **Docker Compose**: Orquestração de múltiplos containers
- **psycopg2**: Driver para conexão Python-PostgreSQL

## Como Executar

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Git

### Passos para Execução

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/pereiraR3/Activity-Network2.git
   cd Activity-Network2
   ```

2. **Execute os containers com Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Acesse a aplicação:**
   - A aplicação estará disponível em: `http://localhost:5000`
   - Endpoint de teste: `http://localhost:5000/db_version`

### Comandos Úteis

```bash
# Parar os containers
docker-compose down

# Visualizar logs
docker-compose logs

# Executar em background
docker-compose up -d

# Rebuild dos containers
docker-compose build --no-cache
```

## Configuração

### Variáveis de Ambiente

A aplicação utiliza as seguintes variáveis de ambiente para conectar ao banco de dados:

| Variável | Valor Padrão | Descrição |
|----------|--------------|-----------|
| `DB_HOST` | `db` | Host do banco de dados |
| `DB_PORT` | `5432` | Porta do PostgreSQL |
| `DB_NAME` | `bancoRedes2` | Nome do banco de dados |
| `DB_USER` | `postgres` | Usuário do banco |
| `DB_PASSWORD` | `12345` | Senha do banco |

### Docker Compose

O arquivo `docker-compose.yml` define dois serviços:

- **app**: Container da aplicação Flask
- **db**: Container do PostgreSQL

## Endpoints da API

### GET /db_version

Retorna a versão do banco de dados PostgreSQL conectado.

**Resposta de Sucesso:**
```json
{
  "db_version": "PostgreSQL 16.0 on x86_64-pc-linux-gnu..."
}
```

**Resposta de Erro:**
```json
{
  "error": "Mensagem de erro"
}
```

## Detalhes dos Containers

### Container da Aplicação (app)

- **Base**: `python:3.10-slim`
- **Porta**: `5000`
- **Build**: Multi-stage build clonando o repositório Git
- **Dependências**: Flask, psycopg2-binary

### Container do Banco (db)

- **Imagem**: `postgres:latest`
- **Porta**: `5432`
- **Volume**: Persistência de dados com `postgres_data`

## Requisitos Atendidos

✅ **Aplicação simples conectando ao banco de dados**
- Aplicação Flask com endpoint funcional

✅ **Repositório no GitHub**
- Código versionado e disponível publicamente

✅ **Docker Compose com múltiplos containers**
- Container para aplicação e container para banco de dados

✅ **Variáveis de ambiente para credenciais**
- Configuração segura através de variáveis de ambiente

✅ **Docker build clonando repositório**
- Dockerfile com multi-stage build clonando do GitHub

## Equipe

- **Desenvolvedor**: [Anthony R. R. Rezende](https://github.com/pereiraR3), [Vinícius P. Vieira](https://github.com/vnny8), [Enzo Magalhães](https://github.com/Enzo-Campos-2025), [Alan Bruno](https://github.com/AlanBMC)
- **Repositório**: [pereiraR3/Activity-Network2](https://github.com/pereiraR3/Activity-Network2)
