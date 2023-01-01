from app.candidates.dao.candidates_dao import CandidateDao
import pytest
from utils import get_config


@pytest.fixture()
def candidates_dao():
    return CandidateDao(get_config().PATH)


keys_should_be = {"pk", "name", "position"}


class TestCandidateDao:
    def test_get_all(self, candidates_dao):
        candidates: list[dict] = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_pk(self, candidates_dao):
        candidate = candidates_dao.get_by_pk(1)
        assert candidate['pk'] == 1, "возвращается неправильный кандидат"
        assert set(candidate.keys()) == keys_should_be, "неверный список ключей"

    def test_file_location(self, candidates_dao):
        with pytest.raises(FileNotFoundError):
            CandidateDao('random_path').load_data()
