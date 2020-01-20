from flask import Blueprint
from requests.exceptions import RequestException
from extensions import giphyApi

blueprint = Blueprint("gif", __name__)


@blueprint.route("/api/gifs/search/<query>")
def search_gifs(query):
    try:
        results = giphyApi.search(query)
        return results, 200
    except RequestException:
        return {"message": "Internal Server Error"}, 500


@blueprint.route("/api/gifs/<query>")
def get_gifs(query):
    try:
        results = giphyApi.get(query)
        return results, 200
    except RequestException:
        return {"message": "Internal Server Error"}, 500
