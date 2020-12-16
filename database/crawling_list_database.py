#!/usr/bin/env python
import os
import sys
from .base_database import BaseDatabase
from .crawling_list_vo import CrawlingListVo
from datetime import datetime
import logging

class CrawlingListDatabase(BaseDatabase):
    TABLE_NAME = "CRAWLING_LIST"

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(100) NOT NULL")
        field_list.append("url varchar(512) NOT NULL")
        field_list.append("type varchar(20) NOT NULL")
        field_list.append("is_analysis bool NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)
    ######################################################################
    # common
    def __exist_all(self):
        return self.exist_data(self.TABLE_NAME)

    def __select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, CrawlingListVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, CrawlingListVo.get_select_query())

    def __select_one(self, where_string):
        return self.select_one(self.TABLE_NAME, CrawlingListVo.get_select_query(), where_string)

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
        return CrawlingListVo(row)
    ######################################################################
    # select
    def select_list_by_no_analysis(self):
        where_string = "is_analysis = 0"
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_list_by_no_analysis_service(self, service_name):
        where_string = "is_analysis = 0 and name like '{}:%'".format(service_name)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    ######################################################################
    # insert
    def insert_service_info(self, service_name, url):
        type = "SERVICE_INFO"
        return self.insert_info(service_name, url, type)

    def insert_command_info(self, service_name, command_name, url):
        type = "COMMAND_INFO"
        name = f"{service_name}:{command_name}"
        return self.insert_info(name, url, type)

    def insert_sub_command_info(self, service_name, command_name, sub_command_name, url):
        type = "SUB_COMMAND_INFO"
        name = f"{service_name}:{command_name}:{sub_command_name}"
        return self.insert_info(name, url, type)

    def insert_info(self, name, url, type):
        now = datetime.now()

        value_string = f"'{name}', '{url}', '{type}', 0, '{now}', '{now}'"
        return self.__insert_data("name, url, type, is_analysis, created_at, updated_at", value_string)


    ######################################################################
    # update
    def check_analysis(self, id):
        set_data = "is_analysis = 1"
        where_string = "id = %d" % (id,)
        self.__update_data(set_data, where_string)

    ######################################################################
    # count
    def exist_all(self):
        return self.__exist_all()

    def delete_all(self):
        return self.delete_all(self.TABLE_NAME)
