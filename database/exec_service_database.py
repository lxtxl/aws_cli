import os
import sys
from .base_database import BaseDatabase
from datetime import date, datetime
import logging
from .ExecServiceVo import ExecServiceVo


class ExecServiceDatabase(BaseDatabase):
    TABLE_NAME = "EXEC_SERVICE"
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
        field_list.append("service_name varchar(100) NOT NULL")
        field_list.append("description varchar(1024) NOT NULL")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    def count_exec_service(self, name):
        where_string = "name = '{}'".format(name)
        return self.select_count("aws_execservice", where_string)

    def insert_exec_service(self, name, service_name, description):
        now = datetime.now()
        replace_description = description.replace("'", "''")
        value_string = "'{}', '{}', '{}'".format(name, service_name, replace_description)
        return self.insert_data("aws_execservice", "name, service_name, description", value_string)

    def select_exec_service_id(self, name):
        where_string = "name = '%s'" % (name,)
        row = self.select_one("aws_execservice", "id", where_string)

        if row == None:
            return None
        return int(row[0])

    def select_exec_service_one(self, name):
        where_string = "name = '%s'" % (name, )
        row = self.select_one("aws_execservice", ExecServiceVo.get_select_query(), where_string)

        if row == None:
            return None

        exec_service = ExecServiceVo(row)
        return exec_service

    def select_distinct_exec_service(self):
        rows = self.select_distinct("aws_execservice", "service_name")

        awsServiceList = []
        for row in rows:
            awsServiceList.append(row[0])
        return awsServiceList

    def select_exec_service_list_by_service_name(self, service_name):
        where_string = "service_name = '{}'".format(service_name)
        rows = self.select_where("aws_execservice", ExecServiceVo.get_select_query(), where_string)

        exec_service_list = []
        for row in rows:
            exec_service = ExecServiceVo(row)
            exec_service_list.append(exec_service)

        return exec_service_list

    def select_exec_service_list(self):
        rows = self.select_all_asc("aws_execservice", ExecServiceVo.get_select_query(), "service_name")

        exec_service_list = []
        for row in rows:
            exec_service = ExecServiceVo(row)
            exec_service_list.append(exec_service)

        return exec_service_list
