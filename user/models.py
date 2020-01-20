from extensions import db, bcrypt


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    gifs = db.ListField(db.URLField(default=[]))

    def hash_password(self):
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf8')
