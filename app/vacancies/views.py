from flask import Blueprint, render_template
from .dao.vacancies_dao import VacanciesDAO
from utils import get_config

vacancies_blueprint = Blueprint('vacancies_blueprint', __name__, template_folder="templates")

# Создаем DAO для вакансий
vacancies_dao = VacanciesDAO(get_config().PATH_VACANCIES)


@vacancies_blueprint.route('/vacancies')
def page_vacancies():
    vacancies = vacancies_dao.get_all()
    return render_template("vacancies_index.html", vacancies=vacancies)


@vacancies_blueprint.route('/vacancies/<int:pk>')
def page_vacancy(pk):
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template("vacancies_single.html", vacancy=vacancy)