from flask import Blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def main_blp():
    return 'Я главная страничка'
