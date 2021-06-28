from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env

from app import views

env = Env()
env.read_env()

db = SQLAlchemy()
mg = Migrate()


def create_app():
    # Configs do app
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    # Inicialização dos modulos
    db.init_app(app)
    from app.models import CategoryModel
    from app.models import EisenhowerModel
    from app.models import TaskCategoryModel
    from app.models import TaskModel


    mg.init_app(app, db)
    views.init_app(app)

    # with app.app_context():
    #    db.create_all()  # IF NOT EXISTS

    return app
