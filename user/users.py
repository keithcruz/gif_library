from flask import Blueprint

blueprint = Blueprint("user", __name__)


@blueprint.route("/users/<id>")
def get_user(id):
    return {"id": id}
