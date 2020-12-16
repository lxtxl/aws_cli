#!/usr/bin/python


class SubCommandOutputVo:
    id = 0
    created_at = ""
    updated_at = ""
    command_id = 0
    name = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.created_at = row[1]
        self.updated_at = row[2]
        self.command_id = int(row[3])
        self.name = row[4]

    @classmethod
    def get_select_query(cls):
        return "id, created_at, updated_at, command_id, name"

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def __str__(self):
        return "{} => {}".format(self.id, self.name)