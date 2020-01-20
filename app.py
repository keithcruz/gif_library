from flask import Flask

from extensions import db, bcrypt
from gif import gifs
from user import users


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("ENV_FILE")

    register_blueprints(app)

    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(gifs.blueprint)
    app.register_blueprint(users.blueprint)


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
