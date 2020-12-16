#!/usr/bin/python


class ExecServiceVo:
    id = 0
    name = ""
    service_name = ""
    description = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.service_name = row[2]
        self.description = row[3]

    @classmethod
    def get_select_query(cls):
        return "id, name, service_name, description"

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getServiceName(self):
        return self.service_name

    def getDescription(self):
        return self.description

    def __str__(self):
        return "{} => {} {} {}".format(self.id, self.name, self.service_name, self.description)