from database import db


class Autor(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    nacionalidade = db.Column(db.String(50), nullable=True)

    def _repr__(self):
        return f"<Nome {self.nome}>"

    livros = db.relationship('Livro', backref='autor', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)

    def _repr__(self):
        return f"<Nome {self.nome}>"


class Livro(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    data_publicacao = db.Column(db.Date, nullable=True)
    numero_paginas = db.Column(db.Integer, nullable=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    categoria_id = db.Column(db.String, db.ForeignKey('categorias.id'), nullable=False)

    def _repr__(self):
        return f"<Nome {self.titulo}>"

    categorias = db.relationship('Civro', backref='livros', lazy=True)

with app.app_context():
    db.create_all()