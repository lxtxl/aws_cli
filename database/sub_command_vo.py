#!/usr/bin/python


class SubCommandVo:
    id = 0
    name = ""
    service_name = ""
    command_name = ""
    url = ""
    is_example_analysis = False
    is_option_analysis = False
    is_output_analysis = False
    is_synopsis_analysis = False
    created_at = ""
    updated_at = ""
    type = ""
    command_id = 0

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.service_name = row[2]
        self.command_name = row[3]
        self.type = row[4]
        self.url = row[5]
        self.created_at = row[6]
        self.updated_at = row[7]
        self.command_id = int(row[8])

    @classmethod
    def get_select_query(cls):
        return "id, name, service_name, command_name, type, url, created_at, updated_at, command_id"

    def __str__(self):
        return "{} => {} {} {} {}".format(self.id, self.name, self.service_name, self.command_name, self.url)
