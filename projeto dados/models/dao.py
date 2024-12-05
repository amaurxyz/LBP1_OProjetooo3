class BaseDAO:
    def __init__(self, model):
        self.model = model

    def adicionar(self, objeto):
        db.session.add(objeto)
        db.session.commit()

    def atualizar(self):
        db.session.commit()

    def excluir(self, objeto):
        db.session.delete(objeto)
        db.session.commit()

    def buscar_por_id(self, título, autor, categoria, isbn):
        return self.model.query.get(titulo)
        return self.model.query.get(autor)
        return self.model.query.get(categoria)
        return self.model.query.get(isbn)

    def listar_todos(self):
        return self.model.query.all()
