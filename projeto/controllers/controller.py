from flask import Blueprint, render_template
from models.model import pessoa

pessoaController = Blueprint('pessoaController', __name__)


@pessoaController.route("/")
def hello_world():
    return render_template("index.html")

@pessoaController.route("/pessoa")
def exibir_pessoa():
    return render_template("pessoa.html", pessoa=pessoa)
