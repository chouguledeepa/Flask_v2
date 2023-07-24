# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

"""
DAL : data Aess Layer
This models to ontain to store and retrive the data
"""

import json


def load_db():
    file_path = ("C:\\Users\\LENOVO\\PycharmProjects\\flask_v2\\modals\\flashard_db.json")
    with open(file_path, "r") as foo:
        return json.load(foo)


db = load_db()
