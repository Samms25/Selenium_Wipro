import json


class TestDataReader:

    def __init__(self, file_path="test_data/user.json"):
        self.file_path = file_path

    def read_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)