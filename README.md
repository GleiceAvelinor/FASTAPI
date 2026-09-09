```markdown
# 🚀 Estudo de FastAPI, Pydantic e Programação Assíncrona com Python

Este repositório contém exemplos práticos e didáticos sobre a criação de APIs web com **FastAPI**, validação e tipagem de dados com **Pydantic** e manipulação de corrotinas assíncronas com **Asyncio** em Python.

---

## 📁 Estrutura do Projeto

* `app.py`: Aplicação FastAPI demonstrando rotas GET e POST, além de execução com servidor Uvicorn.
* `tipo.py`: Exemplo isolado de criação e validação de modelos de dados usando a biblioteca Pydantic.
* `async.py`: Exemplo prático de execução paralela/assíncrona de tarefas utilizando a biblioteca `asyncio`.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework web rápido e moderno para construção de APIs.
* **Pydantic**: Validação de dados e garantias de tipos em tempo de execução.
* **Uvicorn**: Servidor ASGI rápido para rodar aplicações FastAPI.
* **Asyncio**: Biblioteca padrão do Python para escrita de código concorrente via `async/await`.

---

## 📦 Configuração e Instalação

1. **Clone o repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>

```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

```


3. **Instale as dependências:**
```bash
pip install fastapi uvicorn pydantic

```



---

## 💻 Como Executar os Arquivos

### 1. API Web (`app.py`)

Para iniciar o servidor FastAPI da aplicação:

```bash
python app.py

```

A API estará disponível no endereço: `http://127.0.0.1:3000`

#### 📌 Endpoints disponíveis:

* **`GET /saudar/{nome}`**: Retorna uma mensagem de saudação personalizada.
* **`POST /usuarios`**: Recebe um JSON com os dados do usuário e o cria (retorna confirmação e dados).
* **`GET /usuarios`**: Retorna os dados passados no corpo da requisição.

> 💡 **Documentação Interativa (Swagger UI):**
> Com o servidor rodando, acesse `http://127.0.0.1:3000/docs` para testar as rotas interativamente.

---

### 2. Validação com Pydantic (`tipo.py`)

Para testar a validação de tipos e coerção automática (ex: conversão automática da string `"30"` para inteiro `30`):

```bash
python tipo.py

```

---

### 3. Concorrência Assíncrona (`async.py`)

Para entender como tarefas assíncronas funcionam em paralelo vs. sequencialmente:

```bash
python async.py

```

* O script dispara as tarefas `1` e `2` simultaneamente através do `asyncio.gather` e, após a conclusão, executa a tarefa `3`.

---

## 📄 Exemplo de Payload JSON (para `POST /usuarios`)

```json
{
  "nome": "Rafael",
  "idade": 30,
  "email": "usuario@gmail.com",
  "ativo": true
}

```

```

```