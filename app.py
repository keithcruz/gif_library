from flask import Flask

from config import Config
from extensions import db, bcrypt
from gif import gifs
from user import users


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_blueprints(app)

    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(gifs.blueprint)
    app.register_blueprint(users.blueprint)


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
