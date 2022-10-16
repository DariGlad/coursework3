from flask import Blueprint, jsonify
import logging

from config import LOG_PATH, POST_DATA
from main.dao.post_dao import PostDAO

api_blueprint = Blueprint("api_blueprint", __name__)

# Создаём лог доступа к страничкам api
log_api = logging.getLogger("api")
log_api.setLevel(logging.INFO)
file_handler_log_api = logging.FileHandler(LOG_PATH, encoding="utf-8")
log_api.addHandler(file_handler_log_api)

# Создаём формат логов
format_log_api = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler_log_api.setFormatter(format_log_api)

posts_data = PostDAO(POST_DATA)  # Создаём экземпляр класса постов


@api_blueprint.route("/post/")  # Страничка api всех постов
def page_all_api():
    log_api.info("Доступ к данным api всех постов")
    posts = posts_data.load_data()
    return jsonify(posts)


@api_blueprint.route("/post/<int:post_id>/")  # Страничка  api одного поста
def page_api_on_request(post_id):
    log_api.info(f"Доступ к данным api поста №{post_id}")
    post = posts_data.get_api_post(post_id)
    return jsonify(post)
