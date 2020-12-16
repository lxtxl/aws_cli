import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from .base_database import BaseDatabase
import logging
from datetime import date, datetime
from .sub_command_output_vo import SubCommandOutputVo


class SubCommandOutputDatabase(BaseDatabase):
    TABLE_NAME = "SUB_COMMAND_OUTPUT"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name text NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("sub_command_id integer NOT NULL REFERENCES SUB_COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, SubCommandOutputVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, SubCommandOutputVo.get_select_query())

    def select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, SubCommandOutputVo.get_select_query(), where_string)

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
        return SubCommandOutputVo(row)

    def insert_command_output(self, sub_command_id, depth, output_type, name, original_name, description):
        now = datetime.now()
        if description is None:
            description = ""
        replace_description = description.replace("'", "''")

        value_string = "'{}', '{}', {}, '{}', '{}', {}".format(name, original_name, depth, output_type, replace_description, sub_command_id)
        return self.insert_data("name, original_name, depth, output_type, description, sub_command_id", value_string)

    def select_output_one(self, sub_command_id):
        where_string = f"sub_command_id = {sub_command_id}"
        row = self.select_one(where_string)
        return self.change_object(row)
