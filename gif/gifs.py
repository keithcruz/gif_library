from flask import Blueprint
from flask_jwt_extended import jwt_required
from requests.exceptions import RequestException
from webargs import fields
from webargs.flaskparser import use_args

from extensions import giphyApi

blueprint = Blueprint("gif", __name__)

search_args = {"q": fields.Str(required=True)}

get_args = {"ids": fields.Str(required=True)}


@blueprint.route("/api/gifs/search")
@use_args(search_args, locations=["query"])
@jwt_required
def search_gifs(args):
    try:
        results = giphyApi.search(args.get("q"))
        return results, 200
    except RequestException:
        return {"message": "Internal Server Error"}, 500


@blueprint.route("/api/gifs")
@use_args(get_args, locations=["query"])
@jwt_required
def get_gifs(args):
    try:
        results = giphyApi.get(args.get("ids"))
        return results, 200
    except RequestException:
        return {"message": "Internal Server Error"}, 500
