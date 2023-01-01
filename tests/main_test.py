import pytest


class TestMain:
    def test_root_status(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус всех кодов неверный'

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert 'Я главная страничка' in response.data.decode("utf-8"), "Контент страницы неверный"
