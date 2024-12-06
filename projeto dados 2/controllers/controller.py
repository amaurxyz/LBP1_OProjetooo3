from flask import render_template, Blueprint, request, redirect
from models.model import Livro, Autor, Categoria
from models.rp import LivroRepository, AutorRepository, CategoriaRepository

Controller = Blueprint('Controller',__name__)

livro_repo = LivroRepository()
autor_repo = AutorRepository()
categoria_repo = CategoriaRepository()

@Controller.route("/")
def index():
    return render_template('index.html')

@Controller.route("/livros")
def livros():
    return render_template('livros.html')

@Controller.route('/livros/adicionar', methods=['POST'])
def adicionar_livro():
    titulo = request.form['titulo']
    isbn = request.form['isbn']
    data_publicacao = request.form['data_publicacao']
    numero_paginas = request.form['numero_paginas']
    autor_id = request.form['autor']
    categoria_id = request.form['categoria']
    novo_livro = Livro(titulo=titulo, isbn=isbn, data_publicacao=data_publicacao, 
                       numero_paginas=numero_paginas, autor_id=autor_id, categoria_id=categoria_id)
    livro_repo.adicionar(novo_livro)
    return redirect('/livros')

@Controller.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    livro = livro_repo.buscar_por_id(id)
    if request.method == 'POST':
        livro.titulo = request.form['titulo']
        livro.isbn = request.form['isbn']
        livro.data_publicacao = request.form['data_publicacao']
        livro.numero_paginas = request.form['numero_paginas']
        livro.autor_id = request.form['autor']
        livro.categoria_id = request.form['categoria']
        livro_repo.atualizar()
        return redirect('/livros')
    autores = autor_repo.listar_todos()
    categorias = categoria_repo.listar_todos()
    return render_template('editar_livro.html', livro=livro, autores=autores, categorias=categorias)

@Controller.route('/livros/excluir/<int:id>')
def excluir_livro(id):
    livro = livro_repo.buscar_por_id(id)
    livro_repo.excluir(livro)
    return redirect('/livros')

@Controller.route('/autores')
def autores():
    return render_template('autores.html', autores=autor_repo.listar_todos())

@Controller.route('/autores/adicionar', methods=['POST'])
def adicionar_autor():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    nacionalidade = request.form['nacionalidade']
    novo_autor = Autor(nome=nome, data_nascimento=data_nascimento, nacionalidade=nacionalidade)
    autor_repo.adicionar(novo_autor)
    return redirect('/autores')

@Controller.route('/categorias')
def categorias():
    return render_template('categorias.html', categorias=categoria_repo.listar_todos())

@Controller.route('/categorias/adicionar', methods=['POST'])
def adicionar_categoria():
    nome = request.form['nome']
    nova_categoria = Categoria(nome=nome)
    categoria_repo.adicionar(nova_categoria)
    return redirect('/categorias')

@Controller.route('/livros/buscar', methods=['GET'])
def buscar_livros():
    titulo = request.args.get('titulo')
    autor_id = request.args.get('autor')
    categoria_id = request.args.get('categoria')
    isbn = request.args.get('isbn')

    if titulo:
        livros = livro_repo.buscar_por_titulo(titulo)
    elif isbn:
        livros = livro_repo.buscar_por_isbn(isbn)
    elif autor_id:
        livros = livro_repo.listar_por_autor(autor_id)
    elif categoria_id:
        livros = livro_repo.applistar_por_categoria(categoria_id)
    else:
        livros = livro_repo.listar_todos()

    return render_template('livros.html', livros=livros)