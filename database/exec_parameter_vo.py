#!/usr/bin/python


class ExecParameterVo:
    id = 0
    name = ""
    order_num = 0
    value_type = ""
    execCommand_id = 0
    description = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.order_num = int(row[2])
        self.value_type = row[3]
        self.execCommand_id = int(row[4])
        self.description = row[5]

    @classmethod
    def get_select_query(cls):
        return "id, name, order_num, value_type, execCommand_id, description"

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDescription(self):
        return self.descritpion

    def __str__(self):
        return "{} => {} {} {} {} {}".format(self.id, self.name, self.order_num, self.value_type, self.execCommand_id, self.description)