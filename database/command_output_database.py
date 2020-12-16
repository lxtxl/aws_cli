import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime


class CommandOutputDatabase(BaseDatabase):
    TABLE_NAME = "COMMAND_OUTPUT"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(512) NOT NULL")
        field_list.append("original_name varchar(512) NOT NULL")
        field_list.append("depth smallint unsigned NOT NULL CHECK (depth >= 0)")
        field_list.append("output_type varchar(100) NOT NULL")
        field_list.append("description varchar(1024) NOT NULL")
        field_list.append("command_id integer NOT NULL REFERENCES COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, CommandOutputVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, CommandOutputVo.get_select_query())

    def select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, OutputOutputVo.get_select_query(), where_string)

    def update_data(self, set_data, where_string):
        self.update_data(self.TABLE_NAME, set_data, where_string)

    def select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def insert_data(self, column_string, value_string):
        return self.insert_common_data(self.TABLE_NAME, column_string, value_string)

    def change_object_list(self, rows):
        output_datas = []
        for row in rows:
            output_data = self.change_object(row)
            output_datas.append(output_data)
        return output_datas

    def change_object(self, row):
        if row == None:
            return None
        return CommandOutputVo(row)

    def insert_command_output(self, command_id, depth, output_type, name, original_name, description):
        now = datetime.now()
        if description is None:
            description = ""
        replace_description = description.replace("'", "''")

        value_string = "'{}', '{}', {}, '{}', '{}', {}".format(name, original_name, depth, output_type, replace_description, command_id)
        return self.insert_data("name, original_name, depth, output_type, description, command_id", value_string)

    def select_output_one(self, command_id):
        where_string = f"command_id = {command_id}"
        row = self.select_one(where_string)
        return self.change_object(row)

    def select_jmespath(self, command_id):
        where_string = f"command_id = {command_id} and output_type in ('STRUCTURE', 'STRING', 'TIMESTAMP') and depth < 2"
        rows = self.select_where(where_string)

        is_array = False
        depth0_name = ""
        depth1_list = []
        available_list = ["TIMESTAMP", "STRING"]
        skip_list = ["STRUCTURE"]
        for row in rows:
            command_output = self.change_object(row)
            if command_output.depth == 0 and "->(structure)" in command_output.name:
                is_array = True
                depth0_name = command_output.name.replace("->(structure)", "")
            elif command_output.name == "(string)":
                continue
            elif command_output.depth == 0 and command_output.output_type in available_list:
                depth1_list.append(command_output.name)
            elif command_output.depth == 1 and command_output.output_type in available_list:
                depth1_list.append(command_output.name)
            elif command_output.depth == 1 and command_output.output_type in skip_list:
                continue
            else:
                print(f"오류가 발생했습니다. {command_output}")
                sys.exit(1)

        if is_array:
            if len(depth1_list) > 0:
                return "{}[*].[{}]".format(depth0_name, ",".join(depth1_list))
            else:
                return "{}[*]".format(depth0_name)
        return "{}".format(",".join(depth1_list))


class CommandOutputVo:

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.original_name = row[2]
        self.depth = int(row[3])
        self.output_type = row[4]
        self.description = row[5]
        self.command_id = int(row[3])

    @classmethod
    def get_select_query(cls):
        return "id, name, original_name, depth, output_type, description, command_id"

    def __str__(self):
        return "{} => {}".format(self.id, self.name)

