from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        task = request.form["task"]
        desc = request.form["desc"]
        tarefa = {
            "task": task,
            "desc": desc
        }
        tarefas.append(tarefa)
        return f"Tarefa Cadastrada"

@app.route("/Visualizar", methods=["GET"])
def visualizar():
    return render_template("Visualizar.html", tarefas = tarefas)


app.run(debug=True)