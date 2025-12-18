from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '5d4b4a1acdf7c0e4b22f47cef267c9be'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    db.init_app(app)

    from src import routes, models
    app.register_blueprint(routes.main)

    with app.app_context():
        db.create_all()

    return app
