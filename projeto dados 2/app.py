from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.controller import Controller

app = Flask(__name__)

app.register_blueprint(Controller)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///examplee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__=='__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
