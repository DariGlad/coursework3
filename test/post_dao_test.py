import pytest

from classes.post import Post
from config import POST_DATA
from main.dao.post_dao import PostDAO

data = PostDAO(POST_DATA)


class TestPostDAO:
    def test_load_data(self):
        """ Тест для проверки метода load_data класса PostDAO """
        assert isinstance(data.load_data(), list), "Неверный тип данных"

    def test_get_api_post(self):
        assert isinstance(data.get_api_post(1), dict), "Неверный тип данных"

    def test_get_posts_all(self):
        assert isinstance(data.get_posts_all(), list), "Неверный тип данных"

    def test_get_posts_by_user(self):
        assert isinstance(data.get_posts_by_user("leo"), list), "Неверный тип данных"
        with pytest.raises(ValueError):
            data.get_posts_by_user(""), "Не отрабатывает ошибка ValueError"

    def test_search_for_posts(self):
        assert isinstance(data.search_for_posts("в"), list), "Неверный тип данных"

    def test_get_post_by_pk(self):
        assert isinstance(data.get_post_by_pk(1), Post), "Не принадлежит классу Post"
