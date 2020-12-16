#!/usr/bin/python


class ServiceCommandVo:
    id = 0
    name = ""
    url = ""
    service_name = ""
    type = ""
    group_name = ""
    is_many = False


    # id, name, is_analysis, description, createdAt, updatedAt
    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.url = row[2]
        self.service_name = row[3]
        self.type = row[4]
        self.group_name = row[5]
        self.is_many = bool(row[6])

    def print(self):
        print("{} => {} ({})".format(self.id, self.name, self.service_name))

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getServiceName(self):
        return self.service_name

