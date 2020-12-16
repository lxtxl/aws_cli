#!/usr/bin/python


class CommandExampleVo:
    id = 0
    name = ""
    created_at = ""
    updated_at = ""
    command_id = 0

    # id, name, is_analysis, description, createdAt, updatedAt
    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.created_at = row[2]
        self.updated_at = row[3]
        self.command_id = int(row[4])

    @classmethod
    def get_select_query(cls):
        return "id, name, created_at, updated_at, command_id"

    def __str__(self):
        return "{} => {} {}".format(self.id, self.name, self.command_id)