from flask import Flask

from gif import gifs
from user import users


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(gifs.blueprint)
    app.register_blueprint(users.blueprint)
