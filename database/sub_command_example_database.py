import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime
from .sub_command_example_vo import SubCommandExampleVo


class SubCommandExampleDatabase(BaseDatabase):
    TABLE_NAME = "SUB_COMMAND_EXAMPLE"

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
        field_list.append("sub_command_id integer NOT NULL REFERENCES SUB_COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def __select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, SubCommandExampleVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, SubCommandExampleVo.get_select_query())

    def __select_one(self, where_string):
        return self.__select_one(self.TABLE_NAME, SubCommandExampleVo.get_select_query(), where_string)

    def __update_data(self, set_data, where_string):
        self.__update_data(self.TABLE_NAME, set_data, where_string)

    def __select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def __insert_data(self, column_string, value_string):
        return self.insert_common_data(self.TABLE_NAME, column_string, value_string)

    def __change_object_list(self, rows):
        datas = []
        for row in rows:
            data = self.__change_object(row)
            datas.append(data)
        return datas

    def __change_object(self, row):
        if row == None:
            return None
        return SubCommandExampleVo(row)

    def insert_sub_command_example(self, sub_command_id, name):
        now = datetime.now()
        replace_name = name.replace("'", "''")
        value_string = "'%s', '%s', '%s', %d" % (replace_name, now, now, sub_command_id)
        return self.__insert_data("name, created_at, updated_at, sub_command_id", value_string)