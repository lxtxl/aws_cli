import os
import sys
from .base_database import BaseDatabase
from datetime import date, datetime
import logging
from .exec_command_vo import ExecCommandVo


class ExecCommandDatabase(BaseDatabase):
    TABLE_NAME = "EXEC_COMMAND"

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
        field_list.append("command_name varchar(100) NOT NULL")
        field_list.append("parameter_num smallint unsigned NOT NULL CHECK (parameter_num >= 0)")
        field_list.append("jmespath text NOT NULL")
        field_list.append("is_output bool NOT NULL")
        field_list.append("type varchar(20) NOT NULL")
        field_list.append("description varchar(1024) NOT NULL")
        field_list.append("exec_service_name varchar(100) NOT NULL")
        field_list.append("require_parameters varchar(1024) NOT NULL")
        field_list.append("execService_id integer NOT NULL REFERENCES EXEC_SERVICE (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, ExecCommandVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, ExecCommandVo.get_select_query())

    def select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, ExecCommandVo.get_select_query(), where_string)

    def update_data(self, set_data, where_string):
        self.update_data(self.TABLE_NAME, set_data, where_string)

    def select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def insert_data(self, column_string, value_string):
        return self.insert_common_data(self.TABLE_NAME, column_string, value_string)

    def change_object_list(self, rows):
        exec_command_datas = []
        for row in rows:
            exec_command_data = self.change_object(row)
            exec_command_datas.append(exec_command_data)
        return exec_command_datas

    def change_object(self, row):
        if row == None:
            return None
        return ExecCommandVo(row)

    ######################################################################
    # select
    def select_exec_command_one(self, execService_id, name):
        where_string = "execService_id = {} and name = '{}'".format(execService_id, name)
        row = self.select_one(where_string)
        return self.change_object(row)

    def select_exec_command_one(self, execService_id, name):
        where_string = "execService_id = {} and name = '{}'".format(execService_id, name)
        row = self.select_one(where_string)
        return self.change_object(row)
    ######################################################################
    # insert
    def insert_exec_command(self, name, command_name, parameter_num, jmespath, is_output, type, execService_id, description, exec_service_name, require_parameters):
        replace_jmespath = jmespath.replace("'", "''")
        if is_output == True:
            is_output_num = 1
        else:
            is_output_num = 0
        value_string = "'{}', '{}', {}, '{}', {}, '{}', {}, '{}', '{}', '{}'".format(name, command_name, parameter_num, replace_jmespath, is_output_num, type, execService_id, description, exec_service_name, require_parameters)
        return self.insert_data("name, command_name, parameter_num, jmespath, is_output, type, execService_id, description, exec_service_name, require_parameters", value_string)
    ######################################################################
    # update

    ######################################################################
    # count
    def count_exec_command(self, execService_id, name):
        where_string = "execService_id = {} and name = '{}'".format(execService_id, name)
        return self.select_count(where_string)
    ######################################################################

    def select_exec_command_lists(self, exec_service_name):
        where_string = "exec_service_name = '{}'".format(exec_service_name)
        rows = self.select_where(where_string)
        return self.change_object_list(rows)