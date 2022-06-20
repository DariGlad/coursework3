import json

from classes.post import Post


class PostDAO:
    """ Класс доступа к данным постов """

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """ Возвращает данные json (список словарей) """

        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            return data

    def get_api_post(self, post_id):
        """ Возвращает данные json одного поста (словарь)"""

        data = self.load_data()
        post = next((d for d in data if post_id == d["pk"]), None)
        return post

    def get_posts_all(self):
        """ Создаём список классов постов """
        data = self.load_data()
        posts = [Post(d["poster_name"], d["poster_avatar"], d["pic"],
                      d["content"], d["views_count"], d["likes_count"],
                      d["pk"]) for d in data]
        return posts

    # posts = PostDAO("../../data/data.json")
    # print(posts.get_posts_all())

    def get_posts_by_user(self, user_name):
        """ Возвращает посты определенного пользователя """
        data = self.get_posts_all()
        if next((d for d in data if d.poster_name == user_name.lower().strip()), None) is None:
            raise ValueError("Такого пользователя нет")
        posts = [d for d in data if d.poster_name == user_name.lower().strip() and d.content != ""]
        return posts

    # posts = PostDAO("../../data/data.json")
    # print(posts.get_posts_by_user("larry"))

    def search_for_posts(self, query):
        """ Возвращает список постов по ключевому слову """
        data = self.get_posts_all()
        posts = [d for d in data if query.lower() in d.content.lower()]
        return posts

    # posts = PostDAO("../../data/data.json")
    # print(posts.search_for_posts("Утро"))

    def get_post_by_pk(self, pk):
        """ Возвращает один пост по его идентификатору """
        data = self.get_posts_all()
        post = next((d for d in data if pk == d.pk), None)
        return post

# posts = PostDAO("../../data/data.json")
# print(posts.get_post_by_pk(4))
