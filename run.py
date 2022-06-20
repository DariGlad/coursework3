from flask import Flask

from api.views import api_blueprint
from error.views import error_blueprint
from main.views import main_blueprint

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(error_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api/")

if __name__ == "__main__":
    app.run()
