from flask import Flask, Blueprint
from controllers.controller import pessoaController

app = Flask(__name__)

app.register_blueprint(pessoaController)

if __name__ == "__main__":
    app.run(debug=True)