from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from giphyApi import GiphyApi


bcrypt = Bcrypt()
giphyApi = GiphyApi()
jwt = JWTManager()
db = MongoEngine()
