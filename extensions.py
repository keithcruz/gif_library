from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

from giphy_api import GiphyApi


bcrypt = Bcrypt()
giphyApi = GiphyApi()
jwt = JWTManager()
db = MongoEngine()
cors = CORS()
