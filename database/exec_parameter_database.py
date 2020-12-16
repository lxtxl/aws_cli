import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime
from .exec_parameter_vo import ExecParameterVo


class ExecParameterDatabase(BaseDatabase):
    TABLE_NAME = "EXEC_PARAMETER"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(100) NOT NULL")
        field_list.append("order_num integer")
        field_list.append("value_type varchar(20) NOT NULL")
        field_list.append("description varchar(1024) NULL")
        field_list.append("trim_name varchar(100) NOT NULL")
        field_list.append("execCommand_id integer NOT NULL REFERENCES EXEC_COMMAND ('id') DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, ExecParameterVo.get_select_query(), where_string)

    def select_where_asc(self, where_string):
        return self.select_common_where_asc(self.TABLE_NAME, ExecParameterVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, ExecParameterVo.get_select_query())

    def select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, ExecParameterVo.get_select_query(), where_string)

    def update_data(self, set_data, where_string):
        self.update_data(self.TABLE_NAME, set_data, where_string)

    def select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def insert_data(self, column_string, value_string):
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
        return ExecParameterVo(row)

    ######################################################################
    # select

    ######################################################################
    # insert
    def insert_exec_parameter(self, name, order_num, value_type, execCommand_id, trim_name):
        value_string = "'{}', {}, '{}', {}, '{}' ".format(name, order_num, value_type, execCommand_id, trim_name)
        return self.insert_data("name, order_num, value_type, execCommand_id, trim_name", value_string)
    ######################################################################
    # update

    ######################################################################
    # count
    def count_exec_parameter(self, execCommand_id):
        where_string = "execCommand_id = {}".format(execCommand_id)
        return self.select_count(where_string)
    ######################################################################


    def select_exec_parameter_list(self, exec_command_id):
        where_string = "execCommand_id = {}".format(exec_command_id)
        rows = self.select_where_asc("aws_execparameter", ExecParameterVo.get_select_query(), where_string, "order_num")

        exec_parameter_list = []
        for row in rows:
            exec_parameter = ExecParameterVo(row)
            exec_parameter_list.append(exec_parameter)

        return exec_parameter_list
