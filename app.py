import csv
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)

# Caminho do CSV, relativo à pasta deste ficheiro (funciona em qualquer diretoria).
CSV_PATH = Path(__file__).parent / "employees.csv"


def find_employee(username):
    """Procura um colaborador no CSV. Devolve um dicionário ou None."""
    # utf-8-sig: aceita UTF-8 normal e também o UTF-8 com BOM que o Excel grava.
    with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row["username"] == username:
                return row
    return None


@app.route("/")
def index():
    username = request.args.get("username", "").strip()
    employee = None
    searched = False

    if username:
        searched = True
        employee = find_employee(username)

    return render_template(
        "index.html", username=username, employee=employee, searched=searched
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
