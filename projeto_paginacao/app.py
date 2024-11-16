from flask import Flask
from controllers.controller import produtoBlueprint

app = Flask(__name__, template_folder='templates')

app.register_blueprint(produtoBlueprint)

if __name__ == '__main__':
    app.run(debug=True)