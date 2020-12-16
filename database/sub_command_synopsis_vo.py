#!/usr/bin/python


class SubCommandSynopsisVo:
    id = 0
    name = ""
    is_require = False
    created_at = ""
    updated_at = ""
    command_id = 0
    comment = ""
    value_name = ""
    option_name = ""
    is_option_analysis = 0

    # id, name, is_analysis, description, createdAt, updatedAt
    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.is_require = bool(row[2])
        self.created_at = row[3]
        self.updated_at = row[4]
        self.command_id = int(row[5])
        self.comment = row[6]
        self.value_name = row[7]
        self.option_name = row[8]
        self.is_option_analysis = bool(row[9])

    @classmethod
    def get_select_query(cls):
        return "id, name, is_require, created_at, updated_at, command_id, comment, value_name, option_name, " \
               "is_option_analysis "

    def getName(self):
        return self.name

    def makeTrimName(self):
        replace_name = self.name.replace(" <value>", "")
        return replace_name

    def getId(self):
        return self.id

    def getOptionName(self):
        return self.option_name