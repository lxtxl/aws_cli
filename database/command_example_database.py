import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime
from .command_example_vo import CommandExampleVo

class CommandExampleDatabase(BaseDatabase):
    TABLE_NAME = "COMMAND_EXAMPLE"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(1024) NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("command_id integer NOT NULL REFERENCES \"COMMAND\"(\"id\") DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, CommandExampleVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, CommandExampleVo.get_select_query())

    def select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, CommandExampleVo.get_select_query(), where_string)

    def update_data(self, set_data, where_string):
        self.update_data(self.TABLE_NAME, set_data, where_string)

    def select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def __insert_data(self, column_string, value_string):
        return self.insert_common_data(self.TABLE_NAME, column_string, value_string)

    def change_object_list(self, rows):
        datas = []
        for row in rows:
            data = self.change_object(row)
            datas.append(data)
        return datas

    def change_object(self, row):
        if row == None:
            return None
        return CommandExampleVo(row)

    def insert_command_example(self, command_id, name):
        now = datetime.now()
        replace_name = name.replace("'", "''")
        value_string = "'%s', '%s', '%s', %d" % (replace_name, now, now, command_id)
        return self.__insert_data("name, created_at, updated_at, command_id", value_string)