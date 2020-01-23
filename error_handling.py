import webargs
from mongoengine import errors
from requests import RequestException

from user.models import User


def register_errors(app):
    @app.errorhandler(webargs.ValidationError)
    def handle_webargs_validation(err):
        return {"message": "invalid request"}, 422

    @app.errorhandler(errors.ValidationError)
    def handle_mongoengine_validation(err):
        return {"message": "invalid request"}, 422

    @app.errorhandler(422)
    def handle_validation(err):
        return {"message": "invalid request"}, 422

    @app.errorhandler(User.DoesNotExist)
    def handle_user_not_found(err):
        return {"message": "not found"}, 404

    @app.errorhandler(RequestException)
    def handle_requests_exception(err):
        return {"message": "Internal Server Error"}, 500
