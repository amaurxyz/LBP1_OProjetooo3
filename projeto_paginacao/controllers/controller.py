from flask import Blueprint, render_template, request
from models.model import meusprodutos

produtoBlueprint = Blueprint('produtoBlueprint', __name__)

@produtoBlueprint.route('/')
def index():
    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)  # Página atual (padrão: 1)
    produtos_por_pagina = 3  # Quantidade de produtos por página

    # Calcular índices para exibir produtos
    start = (page - 1) * produtos_por_pagina
    end = start + produtos_por_pagina
    produtos_na_pagina = meusprodutos[start:end]

    # Calcular o número total de páginas
    total_produtos = len(meusprodutos)
    total_paginas = (total_produtos + produtos_por_pagina - 1) // produtos_por_pagina

    # Renderizar template HTML
    return render_template(
        'index.html',
        p=produtos_na_pagina,
        page=page,
        total_paginas=total_paginas
    )