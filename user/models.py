from extensions import db, bcrypt


class UserGif(db.EmbeddedDocument):
    gif_id = db.StringField(required=True)
    category = db.StringField(required=True)


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6, max_len=100)
    gifs = db.ListField(db.EmbeddedDocumentField(UserGif), default=list)

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
