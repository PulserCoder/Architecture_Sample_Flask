import json


class CandidateDao:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        try:
            return json.load(open(self.path, 'r', encoding='utf-8'))
        except FileNotFoundError:
            raise FileNotFoundError("Your path isn't correct for your machine, please, check your\
.env or put your own path to config/config_common.py")

    def get_all(self):
        return self.load_data()

    def get_by_pk(self, pk):
        for candidate in self.load_data():
            if candidate['pk'] == pk:
                return candidate
