from marshmallow import fields, Schema


class UserGifSchema(Schema):
    gif_id = fields.String()
    category = fields.String()
    url = fields.Url()


class UserSchema(Schema):
    id = fields.String()
    email = fields.Email()
    gifs = fields.Nested(UserGifSchema, many=True)
