# RH – Pesquisa de Colaborador

Aplicação web mínima (Python + Flask) para o workshop **"AI Security 101 – Desenvolver Código Seguro com IA"**.
Pesquisa um colaborador pelo username num ficheiro CSV local e mostra username, email e morada.

> Todos os dados em `employees.csv` são **fictícios**.

## Estrutura

```
hr-lookup/
├── app.py              # Servidor Flask (lógica)
├── employees.csv       # Dados fictícios
├── requirements.txt    # Dependências (só Flask)
├── templates/
│   └── index.html      # Página (formulário + resultado)
├── static/
│   └── style.css       # Estilo
└── README.md
```

## 1. Instalar o Python (Windows)

1. Descarregar em https://www.python.org/downloads/ (versão 3.10 ou superior).
2. No instalador, **marcar "Add python.exe to PATH"**.
3. Confirmar numa nova janela do PowerShell:

```powershell
python --version
```

## 2. Criar o ambiente virtual

Dentro da pasta do projeto:

```powershell
python -m venv venv
venv\Scripts\activate
```

Deve aparecer `(venv)` no início da linha.

> Se o PowerShell bloquear o script de ativação, corre uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
> ou usa a Linha de Comandos (cmd) em vez do PowerShell.

## 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

## 4. Iniciar a aplicação

```powershell
python app.py
```

## 5. Abrir no browser

Abrir http://127.0.0.1:5000

## 6. Testar

**Username existente:** escrever `ana.exemplo` e clicar em *Pesquisar*.
Deve aparecer o username, o email e a morada.

Outros usernames válidos: `bruno.teste`, `carla.demo`, `diogo.amostra`, `eva.modelo`.

**Username inexistente:** escrever `utilizador.inexistente`.
Deve aparecer a mensagem *Colaborador "utilizador.inexistente" não encontrado.*

Para parar a aplicação: `Ctrl + C` no terminal.
