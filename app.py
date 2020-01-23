from flask import Flask

from extensions import bcrypt, db, giphyApi, jwt, cors
from gif import gifs
from user import users
from error_handling import register_errors


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("ENV_FILE")

    register_blueprints(app)

    register_extensions(app)

    register_errors(app)

    return app


def register_blueprints(app):
    origins = app.config.get("CORS_ORIGIN_WHITELIST")
    cors.init_app(gifs.blueprint, origins=origins)
    cors.init_app(users.blueprint, origins=origins)

    app.register_blueprint(gifs.blueprint)
    app.register_blueprint(users.blueprint)


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    giphyApi.init_app(app)
    jwt.init_app(app)
