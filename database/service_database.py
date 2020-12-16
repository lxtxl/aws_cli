#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime

class ServiceVo:
    id = 0
    name = ""
    url = ""
    version = ""
    created_at = ""
    updated_at = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.url = row[2]
        self.version = row[3]
        self.created_at = row[4]
        self.updated_at = row[5]

    @classmethod
    def get_select_query(cls):
        return "id, name, url, version, created_at, updated_at"

    def __str__(self):
        return "ServiceVo {} => {} {} {}".format(self.id, self.name, self.version, self.url)

class ServiceDatabase(BaseDatabase):
    TABLE_NAME= "SERVICE"

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
        field_list.append("url varchar(512) NOT NULL")
        field_list.append("version varchar(100) NOT NULL")
        field_list.append("description varchar(1024) NULL")
        field_list.append("document_url varchar(2048) NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)
    ######################################################################
    # common
    def __select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, ServiceVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, ServiceVo.get_select_query())

    def __select_one(self, where_string):
        return self.select_common_one(self.TABLE_NAME, ServiceVo.get_select_query(), where_string)

    def __update_data(self, set_data, where_string):
        self.update_data(self.TABLE_NAME, set_data, where_string)

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
        return ServiceVo(row)

    ######################################################################
    # select
    def select_service_all(self):
        rows = self.__select_all()
        return self.__change_object_list(rows)

    # def select_service_analysis(self):
    #     where_string = "is_analysis =0"
    #     rows = self.__select_where(where_string)
    #     return self.__change_object_list(rows)
    #
    def select_service_one(self, service_name):
        where_string = "name = '{}'".format(service_name)
        row = self.__select_one(where_string)
        return self.__change_object(row)
    #
    # def select_service_one_by_id(self, id):
    #     where_string = "id = %d" % (id, )
    #     row = self.__select_one(where_string)
    #     return self.__change_object(row)

    ######################################################################
    # insert
    def insert_service_data_not_exist(self, service_name, url, version, description, link):
        data = self.select_service_one(service_name)
        if data == None:
            self.logger.info("{} insert".format(service_name))
            return self.insert_service_data(service_name, url, version, description, link)
        self.logger.info("{} existed".format(service_name))
        return data.id

    def insert_service_data(self, service_name, url, version, description, document_url_list):
        now = datetime.now()
        replace_description = description.replace("'", "''")
        document_url = ",".join(document_url_list)
        value_string = f"'{service_name}', '{url}', '{version}', '{now}', '{now}', '{replace_description}', '{document_url}'"
        return self.__insert_data("name, url, version, created_at, updated_at, description, document_url", value_string)

    ######################################################################
    # update
    def update_service_analysis(self, service_id):
        set_data = "is_analysis = 1"
        where_string = "id = %d" % (service_id, )
        self.__update_data(set_data, where_string)
