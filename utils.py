from flask import Flask

from api.views import api_blueprint
from error.views import error_blueprint
from main.views import main_blueprint


def create_app():
    app = Flask(__name__)

    app.config["JSON_AS_ASCII"] = False
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    app.register_blueprint(main_blueprint)
    app.register_blueprint(error_blueprint)
    app.register_blueprint(api_blueprint, url_prefix="/api/")
    return app
