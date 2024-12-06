from model import Livro, Autor, Categoria
from dao import BaseDAO

class LivroRepository(BaseDAO):
    def __init__(self):
        super().__init__(Livro)

    def buscar_por_titulo(self, titulo):
        return Livro.query.filter(Livro.titulo.ilike(f'%{titulo}%')).all()

    def buscar_por_isbn(self, isbn):
        return Livro.query.filter_by(isbn=isbn).first()

class AutorRepository(BaseDAO):
    def __init__(self):
        super().__init__(Autor)

class CategoriaRepository(BaseDAO):
    def __init__(self):
        super().__init__(Categoria)
