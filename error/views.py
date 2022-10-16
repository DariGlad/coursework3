from flask import Blueprint, render_template

error_blueprint = Blueprint("error_blueprint", __name__)


@error_blueprint.app_errorhandler(404)  # Обработчик ошибки 404
def page_404(e):
    return render_template("404.html")


@error_blueprint.app_errorhandler(ValueError)  # Обработчик ошибки ValueError
def page_value_error(e):
    return render_template("404.html")


@error_blueprint.app_errorhandler(500)  # Обработчик ошибки 500
def page_500(e):
    return render_template("500.html")
