from run import app

keys = {"poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk"}


def test_page_all_api():
    response = app.test_client().get("/api/post/")
    data = response.json
    assert isinstance(data, list), "Неверный тип данных"
    for d in data:
        assert d.keys() == keys, "Проблема в ключах одного из словарей"


def test_page_api_on_request():
    response = app.test_client().get("/api/post/1/")
    data = response.json
    assert isinstance(data, dict), "Неверный тип данных"
    assert data.keys() == keys, "Проблема в ключах одного из словарей"
