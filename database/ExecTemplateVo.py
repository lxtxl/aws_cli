#!/usr/bin/python


class ExecTemplateVo:
    id = 0
    name = ""
    output_type = ""
    execCommand_id = 0
    query_string = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.output_type = row[2]
        self.execCommand_id = int(row[3])
        self.query_string = row[4]

    @classmethod
    def get_select_query(cls):
        return "id, name, output_type, execCommand_id, query_string"

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getQueryString(self):
        return self.query_string

    def getOutputType(self):
        return self.output_type

    def __str__(self):
        return "{} => {} {} {} {}".format(self.id, self.name, self.output_type, self.execCommand_id, self.query_string)