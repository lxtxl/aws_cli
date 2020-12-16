#!/usr/bin/python

class ExecCommandVo:
    id = 0
    name = ""
    command_name = ""
    parameter_num = 0
    jmespath = ""
    is_output = False
    type = ""
    execService_id = 0
    description = ""
    require_parameters = ""


    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.command_name = row[2]
        self.parameter_num = int(row[3])
        self.jmespath = row[4]
        self.is_output = bool(row[5])
        self.type = row[6]
        self.execService_id = int(row[7])
        self.description = row[8]
        self.require_parameters = row[9]

    @classmethod
    def get_select_query(cls):
        return "id, name, command_name, parameter_num, jmespath, is_output, type, execService_id, description, require_parameters"

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getExecServiceId(self):
        return self.execService_id

    def getType(self):
        return self.type

    def getCommandName(self):
        return self.command_name

    def getParameterNum(self):
        return self.parameter_num

    def getJmespath(self):
        return self.jmespath

    def getDescription(self):
        return self.description

    def getRequireParameters(self):
        return self.require_parameters

    def __str__(self):
        return "{} => {} {} {} {} {} {}".format(self.id, self.name, self.command_name, self.parameter_num, self.is_output, self.type, self.execService_id)
