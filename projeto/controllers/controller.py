from flask import Blueprint, render_template, request, redirect, url_for
from models.model import validacao

loginController = Blueprint('loginController', __name__)

@loginController.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if validacao(nome, senha):
            return redirect(url_for('loginController.dashboard'))
        else:
            error = 'Credências Erradas'
            return render_template("index.html", error=error)
    return render_template("index.html")

@loginController.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
