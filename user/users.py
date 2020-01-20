from flask import Blueprint, request, jsonify
from mongoengine import errors

from user.models import User

blueprint = Blueprint("user", __name__)


@blueprint.route("/api/users/<id>")
def get_user(id):
    try:
        user = User.objects.get(id=id)
        return jsonify(user), 200
    except errors.ValidationError:
        return {"message": "bad request"}, 400
    except User.DoesNotExist:
        return {"message": "not found"}, 404


@blueprint.route("/api/users", methods=["POST"])
def add_user():
    body = request.get_json()

    try:
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {"id": str(id)}, 200
    except errors.ValidationError:
        return {"message": "bad request"}, 400
    except errors.NotUniqueError:
        return {"message": "conflict"}, 409
