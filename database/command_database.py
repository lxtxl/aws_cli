#!/usr/bin/env python
import os
import sys
from database.base_database import BaseDatabase
import logging
from database.service_command import ServiceCommandVo
from datetime import datetime
from database.command_util import get_type, is_many

class CommandVo:
    id = 0
    name = ""
    service_name = ""
    url = ""
    version = ""
    created_at = ""
    updated_at = ""
    type = ""
    group_name = ""
    is_make_exec = False
    is_subcommand = False
    description = ""
    document_url = ""
    require_parameter = ""
    service_id = 0

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.service_name = row[2]
        self.url = row[3]
        self.version = row[4]
        self.created_at = row[5]
        self.updated_at = row[6]
        self.type = row[7]
        self.group_name = row[8]
        self.is_make_exec = bool(row[9])
        self.is_subcommand = bool(row[10])
        self.description = row[11]
        self.document_url = row[12]
        self.require_parameter = int(row[13])
        self.service_id = int(row[14])

    @classmethod
    def get_select_query(cls):
        return "id, name, service_name, url, version, created_at, updated_at, type, group_name, is_make_exec, is_subcommand, description, document_url, require_parameter, service_id"

    def print_simple(self):
        print("{} => {} ({})".format(self.id, self.name, self.service_name))

    def is_read(self):
        if self.type == "list" or self.type == "get":
            return True
        return False

    def __str__(self):
        return f"{self.id} => {self.name} {self.service_name} {self.url} {self.type} {self.group_name}"

class CommandDatabase(BaseDatabase):
    TABLE_NAME = "COMMAND"

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(100) NOT NULL")
        field_list.append("service_name varchar(100) NOT NULL")
        field_list.append("url varchar(512) NOT NULL")
        field_list.append("version varchar(100) NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("type varchar(20) NOT NULL")
        field_list.append("group_name varchar(100) NOT NULL")
        field_list.append("is_make_exec bool NOT NULL")
        field_list.append("is_subcommand bool NOT NULL")
        field_list.append("description varchar(1024) NULL")
        field_list.append("document_url varchar(2048) NOT NULL")
        field_list.append("require_parameter integer DEFAULT 0")
        field_list.append("service_id integer NOT NULL REFERENCES \"SERVICE\"(\"id\") DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def __select_where(self, where_string):
        print(self.TABLE_NAME)
        print(CommandVo.get_select_query())
        print(where_string)
        return self.select_common_where(self.TABLE_NAME, CommandVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, CommandVo.get_select_query())

    def __select_one(self, where_string):
        return self.select_common_one(self.TABLE_NAME, CommandVo.get_select_query(), where_string)

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
        return CommandVo(row)

    ######################################################################
    # select
    def select_other_command_by_group_name(self, service_id, group_name):
        where_string = "service_id != {} and group_name = '{}' ".format(service_id, group_name)
        rows = self.__select_distinct_where(where_string)
        return self.__change_object_list(rows)

    def select_command_analysis(self, where_string):
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_command_all(self):
        rows = self.__select_all()
        return self.__change_object_list(rows)

    def select_command_synopsis_analysis(self):
        return self.select_command_analysis("is_synopsis_analysis = 0")

    def select_command_example_analysis(self):
        return self.select_command_analysis("is_example_analysis = 0")

    def select_command_is_command(self):
        return self.select_command_analysis("is_subcommand = 1")

    def select_command_all_by_service_id(self, service_id):
        where_string = "service_id = %d" % (service_id,)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_command_all_by_service_name(self, service_name):
        where_string = "service_name = '{}'".format(service_name)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_command_one(self, service_name, command_name):
        where_string = f"service_name = '{service_name}' and name = '{command_name}'"
        row = self.__select_one(where_string)
        return self.__change_object(row)

    def select_friend_commands(self, service_id, group_name, command_id):
        where_string = "service_id = {} and group_name = '{}' and id != {}".format(service_id, group_name, command_id)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_friend_commands_by_service_name(self, service_name, group_name, command_id):
        where_string = "service_name = '{}' and group_name = '{}' and id != {}".format(service_name, group_name, command_id)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    ######################################################################
    # insert
    def insert_command_data(self, service_id, service_name, command_name, site_url, version, document_url):
        now = datetime.now()
        type, group_name = get_type(command_name)
        is_many_num = is_many(type)
        value_string = f"'{command_name}', '{service_name}', '{site_url}' , '{version}', '{now}', '{now}', '{type}', '{group_name}', 0, 0, {service_id}, '{document_url}'"
        return self.__insert_data(
            "name, service_name, url, version, created_at, updated_at, type, group_name, is_make_exec, is_subcommand, service_id, document_url",
            value_string)

    def insert_command_data_not_exist(self, service_id, service_name, command_name, site_url, version, document_url):
        data = self.select_command_one(service_name, command_name)
        if data == None:
            self.logger.info("{}/{} insert".format(service_name, command_name))
            return self.insert_command_data(service_id, service_name, command_name, site_url, version, document_url)
        return data.id

    ######################################################################
    # update
    def update_command_by_service_name(self, command_id, service_name):
        set_data = "service_name = '" + service_name + "'"
        where_string = "require_parameter = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_command_by_type_group_name(self, command_id, type_name, group_name, is_many):
        set_data = f"type = '{type_name}', group_name = '{group_name}', is_many = {is_many}"
        where_string = f"id = {command_id}"
        self.__update_data(set_data, where_string)

    def update_command_make_exec(self, service_name, command_name):
        set_data = "is_make_exec = 1"
        where_string = f"service_name = '{service_name}' and name = '{command_name}'"
        self.__update_data(set_data, where_string)

    def update_command_synopsis_analysis(self, command_id):
        set_data = "is_synopsis_analysis = 1"
        where_string = "id = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_command_option_analysis(self, command_id):
        set_data = "is_option_analysis = 1"
        where_string = "id = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_command_output_analysis(self, command_id):
        set_data = "is_output_analysis = 1"
        where_string = "id = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_command_example_analysis(self, command_id):
        set_data = "is_example_analysis = 1"
        where_string = "id = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_is_subcommand_analysis(self, command_id):
        set_data = "is_subcommand_analysis = 1"
        where_string = "id = %d" % (command_id,)
        self.__update_data(set_data, where_string)

    def update_require_parameter_by_service_name_command_name(self, service_name, command_name, require_parameter):
        where_string = "service_name = '{}' and name = '{}'".format(service_name, command_name)
        set_data = "require_parameter = {}".format(require_parameter)
        self.__update_data(set_data, where_string)
    ######################################################################
    # count
    def count_command_synopsis_not_analysis(self):
        where_string = "is_synopsis_analysis = 0"
        return self.__select_count(where_string)

    def count_command_example_not_analysis(self):
        where_string = "is_example_analysis = 0"
        return self.__select_count(where_string)

    def count_command_output_not_analysis(self):
        where_string = "is_output_analysis = 0"
        return self.__select_count(where_string)

    def count_command_option_not_analysis(self):
        where_string = "is_option_analysis = 0"
        return self.__select_count(where_string)
