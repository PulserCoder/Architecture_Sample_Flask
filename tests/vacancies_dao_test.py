from app.vacancies.dao.vacancies_dao import VacanciesDAO
import pytest
from utils import get_config

# Задаем, какие ключи ожидаем получать в вакансии
keys_should_be = {"pk", "company", "position", "salary"}


# Готовим фикстуру, которая даст нам экземпляр DAO
@pytest.fixture()
def vacancies_dao():
    config = get_config()
    vacancies_dao_instance = VacanciesDAO(config.PATH_VACANCIES)
    return vacancies_dao_instance


# Начинаем писать тесты
class TestVacanciesDAO:

    def test_get_all(self, vacancies_dao):
        """ Проверяем получение всех вакансий"""
        vacancies = vacancies_dao.get_all()
        assert type(vacancies) == list
        assert len(vacancies) > 0
        assert set(vacancies[0].keys()) == keys_should_be, set(vacancies[0].keys())

    def test_get_by_pk(self, vacancies_dao):
        """ Проверяем получение одной вакансии"""
        vacancy = vacancies_dao.get_by_pk(1)
        assert type(vacancy) == dict
        assert vacancy["pk"] == 1
        assert set(vacancy.keys()) == keys_should_be
