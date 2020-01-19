from flask import Blueprint

blueprint = Blueprint("gif", __name__)


@blueprint.route("/gifs/<query>")
def get_gifs(query):
    return {"query": query}
