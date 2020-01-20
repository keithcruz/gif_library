from flask import Blueprint

blueprint = Blueprint("gif", __name__)


@blueprint.route("/api/gifs/<query>")
def get_gifs(query):
    return {"query": query}
