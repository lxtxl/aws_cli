import json


class Config:

    def __init__(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)

    def get_database_filename(self):
        return self.config['sqlite3_filename']


    def is_write_db(self):
        return self.config['isWriteDB']
