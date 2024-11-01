from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.model import validacao

loginController = Blueprint('loginController', __name__)

@loginController.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if validacao(nome, senha):
            session['logged'] = True
            flash('Login bem-sucedido!', 'success')
            
            resp = make_response(redirect(url_for('loginController.dashboard')))
            resp.set_cookie('username', nome)
            return resp
        
        flash('Nome ou senha inválidos.', 'danger')

    return render_template('index.html')

@loginController.route("/dashboard")
def dashboard():
    if 'logged' in session:
        return render_template('dashboard.html')
    else:
        flash('Você precisa estar logado para acessar essa página.', 'warning')
        return redirect(url_for('loginController.login'))