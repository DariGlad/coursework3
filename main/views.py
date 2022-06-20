from flask import Blueprint, render_template, abort, request

from config import POST_DATA, COMMENTS_DATA
from main.dao.comments_dao import CommentsDAO
from main.dao.post_dao import PostDAO

main_blueprint = Blueprint("main_blueprint", __name__)

posts_data = PostDAO(POST_DATA)  # Создаём экземпляр класса доступа к данным постов


@main_blueprint.route("/")  # Главная страничка
def main_page():
    posts = posts_data.get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/post/<int:post_id>/")  # Страница поста
def post_page(post_id):
    post = posts_data.get_post_by_pk(post_id)

    if post is None:  # Проверяем, есть ли пост по полученному id, если нет, отправляем в обработчик ошибок 404
        abort(404)

    comments_data = CommentsDAO(COMMENTS_DATA)
    comments = comments_data.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route("/search/")  # Страничка поиска
def search_page():
    posts = ""
    if request.values.get("s"):
        query = request.values.get("s")
        posts = posts_data.search_for_posts(query)
    return render_template("search.html", posts=posts)


@main_blueprint.route("/user/<user_name>/")  # Страничка постов пользователя
def user_page(user_name):
    posts = posts_data.get_posts_by_user(user_name)
    return render_template("user-feed.html", posts=posts)


@main_blueprint.route("/bookmarks/")  # Страничка закладок (в разработке)
def bookmarks_page():
    return "<center><h1>В разработке</h1></center>"
