from flask import Blueprint, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies
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


def generate_tokens(id):
    token = create_access_token(identity=id, fresh=True)
    refresh_token = create_refresh_token(id)
    return {
        "token": token,
        "refreshToken": refresh_token
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

        return generate_tokens(str(user.id)), 200

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

    tokens = generate_tokens(str(user.id))

    resp = jsonify({"login": True})
    resp.set_cookie("my_key", "my_value")
    set_access_cookies(resp, tokens.get("token"))
    set_refresh_cookies(resp, tokens.get("refreshToken"))

    return resp, 200


@blueprint.route("/api/users/refresh")
@jwt_refresh_token_required
def token_refresh():
    user_id = get_jwt_identity()
    new_token = create_access_token(identity=user_id, fresh=False)
    return {"token": new_token}, 200
