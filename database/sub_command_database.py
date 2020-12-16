#!/usr/bin/env python
import os
import sys
from .base_database import BaseDatabase
import logging
from .sub_command_vo import SubCommandVo
from datetime import date, datetime


class SubCommandDatabase(BaseDatabase):
    TABLE_NAME = "SUB_COMMAND"

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
        field_list.append("command_name varchar(100) NOT NULL")
        field_list.append("type varchar(20) NOT NULL")
        field_list.append("url varchar(512) NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("require_parameter integer DEFAULT 0")
        field_list.append("command_id integer NOT NULL REFERENCES COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def __select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, SubCommandVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, SubCommandVo.get_select_query())

    def __select_one(self, where_string):
        return self.select_common_one(self.TABLE_NAME, SubCommandVo.get_select_query(), where_string)

    def __update_data(self, set_data, where_string):
        self.update_common_data(self.TABLE_NAME, set_data, where_string)

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
        return SubCommandVo(row)

    ######################################################################
    # select
    def select_all(self):
        rows = self.__select_all()
        return self.__change_object_list(rows)

    def select_analysis(self, where_string):
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_synopsis_analysis(self):
        return self.select_analysis("is_synopsis_analysis = 0")

    def select_example_analysis(self):
        return self.select_analysis("is_example_analysis = 0")

    def select_option_analysis(self):
        return self.select_analysis("is_option_analysis = 0")

    def select_output_analysis(self):
        return self.select_analysis("is_output_analysis = 0")

    def select_command_one(self, service_name, command_name, sub_command_name):
        where_string = f"service_name = '{service_name}' and command_name = '{command_name}' and name = '{sub_command_name}'"
        row = self.__select_one(where_string)
        return self.__change_object(row)

    ######################################################################
    # insert
    # def insert_service_data_not_exist(self, service_name, url):
    #     data = self.select_service_one(service_name)
    #     if data == None:
    #         self.logger.info("{} insert".format(service_name))
    #         return self.insert_service_data(service_name, url)
    #     self.logger.info("{} existed".format(service_name))
    #     return data.getId()
    #
    def insert_data(self, name, service_name, command_name, url, command_id):
        now = datetime.now()
        value_string = "'{}', '{}', '{}', 'wait', '{}', '{}', '{}', {}".format(name, service_name, command_name, url, now, now, command_id)
        return self.__insert_data("name, service_name, command_name, type, url, created_at, updated_at, command_id",value_string)

    ######################################################################
    # update
    # def update_service_analysis(self, service_id):
    #     set_data = "is_analysis = 1"
    #     where_string = "id = %d" % (service_id, )
    #     self.update_data(set_data, where_string)
    def update_synopsis_analysis(self, sub_command_id):
        set_data = "is_synopsis_analysis = 1"
        where_string = f"id = {sub_command_id}"
        self.__update_data(set_data, where_string)

    def update_command_option_analysis(self, sub_command_id):
        set_data = "is_option_analysis = 1"
        where_string = f"id = {sub_command_id}"
        self.__update_data(set_data, where_string)

    def update_command_output_analysis(self, sub_command_id):
        set_data = "is_output_analysis = 1"
        where_string = f"id = {sub_command_id}"
        self.__update_data(set_data, where_string)

    def update_command_example_analysis(self, sub_command_id):
        set_data = "is_example_analysis = 1"
        where_string = f"id = {sub_command_id}"
        self.__update_data(set_data, where_string)

    def update_require_parameter_by_service_name_command_name_sub_command_name(self, service_name, command_name, sub_command_name, require_parameter):
        where_string = "service_name = '{}' and command_name = '{}' and name = '{}'".format(service_name, command_name, sub_command_name)
        set_data = "require_parameter = {}".format(require_parameter)
        self.__update_data(set_data, where_string)