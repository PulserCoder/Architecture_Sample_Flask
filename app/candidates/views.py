from flask import Blueprint, render_template
from .dao.candidates_dao import CandidateDao
import utils


config = utils.get_config()
candidate_blueprint = Blueprint('candidate_blueprint', __name__, template_folder='templates')
candidates_dao = CandidateDao(config.PATH)


@candidate_blueprint.route('/candidates/')
def show_candidates():
    return render_template('candidates_index.html', candidates=candidates_dao.get_all())


@candidate_blueprint.route('/candidates/<int:pk>')
def show_candidate_by_pk(pk):
    return render_template('candidate_single.html', candidate=candidates_dao.get_by_pk(pk))
