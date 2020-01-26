from flask import Blueprint, jsonify
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies
)
from mongoengine import errors
from webargs import fields, validate
from webargs.flaskparser import use_args

from user.models import User, UserGif
from user.serializers import UserSchema, UserGifSchema

blueprint = Blueprint("user", __name__)

user_schema = UserSchema()


login_args = {
    "email": fields.Email(required=True),
    "password": fields.Str(required=True)
}

register_args = {
    "email": fields.Email(required=True),
    "password": fields.Str(
        required=True, validate=[validate.Length(min=6, max=100)]
    )
}

update_args = {
    "gifs": fields.Nested(UserGifSchema, many=True)
}


@blueprint.route("/api/users", methods=["GET"])
@jwt_required
def get_user():
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    return user_schema.dump(user)


@blueprint.route("/api/users", methods=["POST"])
@use_args(register_args)
def add_user(args):
    try:
        user = User(**args)
        user.hash_password()
        user.save()

        token = create_access_token(str(user.id))

        response = jsonify({"login": True})
        set_access_cookies(response, token)

        return response, 200

    except errors.NotUniqueError:
        return {"message": "conflict"}, 409


@blueprint.route("/api/users", methods=["PUT"])
@use_args(update_args)
@jwt_required
def update_user(args):
    gifs = [UserGif(**gif) for gif in args.get("gifs", [])]

    user_id = get_jwt_identity()
    user = User.objects.get(id=str(user_id))
    user.update(gifs=gifs)
    user.reload()

    return user_schema.dump(user), 200


@blueprint.route("/api/users/login", methods=["POST"])
@use_args(login_args)
def login_user(args):
    user = User.objects.get(email=args.get("email"))
    is_authed = user.verify_password(args.get("password"))

    if not is_authed:
        return {"message": "Invalid credentials"}, 401

    token = create_access_token(str(user.id))

    response = jsonify({"login": True})
    set_access_cookies(response, token)

    return response, 200


@blueprint.route("/api/users/logout", methods=["POST"])
def logout_user():
    resp = jsonify({"logout": True})
    unset_jwt_cookies(resp)
    return resp, 200
