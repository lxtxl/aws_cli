import os
import sys
from .base_database import BaseDatabase
from datetime import date, datetime
import logging
from .ExecTemplateVo import ExecTemplateVo


class ExecTemplateDatabase(BaseDatabase):
    TABLE_NAME = "EXEC_TEMPLATE"
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
        field_list.append("output_type varchar(20) NOT NULL")
        field_list.append("query_string text NOT NULL")
        field_list.append("execCommand_id integer NOT NULL REFERENCES EXEC_COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    def count_exec_base_template(self, execCommand_id):
        where_string = "execCommand_id = {} and name = 'base'".format(execCommand_id)
        return self.select_count("aws_exectemplate", where_string)

    def insert_exec_template(self, name, query_string, output_type, execCommand_id):
        replace_query_string = query_string.replace("'", "''")
        value_string = "'{}', '{}', '{}', {} ".format(name, replace_query_string, output_type, execCommand_id)
        return self.insert_data("aws_exectemplate", "name, query_string, output_type, execCommand_id", value_string)

    def select_exec_template_list(self, exec_command_id):
        where_string = "execCommand_id = {}".format(exec_command_id)
        rows = self.select_where("aws_exectemplate", ExecTemplateVo.get_select_query(), where_string)

        exec_template_list = []
        for row in rows:
            exec_template = ExecTemplateVo(row)
            exec_template_list.append(exec_template)

        return exec_template_list

    def count_exec_template(self, exec_command_id, name):
        where_string = f"execCommand_id = {exec_command_id} and name = '{name}'"
        return self.select_count("aws_exectemplate", where_string)
