class Post:
    """ Класс для хранения поста """
    def __init__(self,
                 poster_name,
                 poster_avatar,
                 pic,
                 content,
                 views_count,
                 likes_count,
                 pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f"Имя постера: {self.poster_name}\n" \
               f"Ссылка постера: {self.poster_avatar}\n" \
               f"Ссылка на картинку: {self.pic}\n" \
               f"Пост пользователя: {self.content}\n" \
               f"Количество просмотров: {self.views_count}\n" \
               f"Количество лайков: {self.likes_count}\n" \
               f"Порядковый номер: {self.pk}\n"
