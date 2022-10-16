import json

from classes.comment import Comment


class CommentsDAO:
    """ Класс доступа к данным комментариев """
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """ Получаем данные из json (список словарей) """

        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            return data

    def get_comments_all(self):
        """ Создаём список клаасов комментариев """
        data = self.load_data()
        comments = [Comment(d["post_id"], d["commenter_name"],
                            d["comment"], d["pk"]) for d in data]
        return comments

    def get_comments_by_post_id(self, post_id):
        """ Возвращает комментарии определённого поста """
        data = self.get_comments_all()
        comments_for_post = [d for d in data if d.post_id == post_id]
        return comments_for_post
