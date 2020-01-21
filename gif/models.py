from extensions import db


class Gif(db.EmbeddedDocument):
    gif_id = db.StringField(required=True)
    category = db.StringField(required=True)
