import pytest

from classes.comment import Comment
from config import COMMENTS_DATA
from main.dao.comments_dao import CommentsDAO

data = CommentsDAO(COMMENTS_DATA)


class TestCommentsDAO:
    def test_load_data(self):
        assert isinstance(data.load_data(), list), "Неверный тип данных"

    def test_get_comments_all(self):
        assert isinstance(data.get_comments_all(), list), "Неверный тип данных"

    def test_get_comments_by_post_id(self):
        assert isinstance(data.get_comments_by_post_id(1), list), "Неверный тип данных"
