from flask import Blueprint
from flask_jwt_extended import jwt_required
from webargs import fields
from webargs.flaskparser import use_args

from extensions import giphyApi

blueprint = Blueprint("gif", __name__)

search_args = {
    "q": fields.Str(required=True),
    "offset": fields.Int()
}


@blueprint.route("/api/gifs/search")
@use_args(search_args, locations=["query"])
@jwt_required
def search_gifs(args):
    results = giphyApi.search(args.get("q"), args.get("offset"))
    return results, 200
