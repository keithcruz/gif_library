from extensions import db, bcrypt
from gif.models import Gif


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    gifs = db.ListField(db.EmbeddedDocumentField(Gif))

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
