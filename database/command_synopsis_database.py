import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime


class CommandSynopsisVo:
    id = 0
    name = ""
    service_name = ""
    command_name = ""
    value_name = ""
    option_name = ""
    is_require = 0
    comment = ""
    created_at = ""
    updated_at = ""
    command_id = 0

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.service_name = row[2]
        self.command_name = row[3]
        self.value_name = row[4]
        self.option_name = row[5]
        self.is_require = bool(row[6])
        self.comment = row[7]
        self.created_at = row[8]
        self.updated_at = row[9]
        self.command_id = int(row[10])

    @classmethod
    def get_select_query(cls):
        return "id, name, service_name, command_name, value_name, option_name, is_require, comment, created_at, updated_at, command_id"

    def getName(self):
        return self.name

    def makeTrimName(self):
        replace_name = self.name.replace(" <value>", "")
        return replace_name

    def getId(self):
        return self.id

    def getOptionName(self):
        return self.option_name


class CommandSynopsisDatabase(BaseDatabase):
    TABLE_NAME="COMMAND_SYNOPSIS"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        field_list = []
        field_list.append("name varchar(300) NOT NULL")
        field_list.append("service_name varchar(100) NOT NULL")
        field_list.append("command_name varchar(100) NOT NULL")
        field_list.append("value_name varchar(300) NOT NULL")
        field_list.append("option_name varchar(300) NOT NULL")
        field_list.append("is_require bool NOT NULL")
        field_list.append("comment text NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("command_id integer NOT NULL REFERENCES COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, CommandSynopsisVo.get_select_query(), where_string)

    def select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def select_all(self):
        return self.select_common_all(self.TABLE_NAME, CommandSynopsisVo.get_select_query())

    def select_one(self, where_string):
        return self.select_common_one(self.TABLE_NAME, CommandSynopsisVo.get_select_query(), where_string)

    def __update_data(self, set_data, where_string):
        self.update_common_data(self.TABLE_NAME, set_data, where_string)

    def select_count(self, where_string):
        return self.select_common_count(self.TABLE_NAME, where_string)

    def insert_data(self, column_string, value_string):
        return self.insert_common_data(self.TABLE_NAME, column_string, value_string)

    def change_object_list(self, rows):
        command_synopsis_datas = []
        for row in rows:
            command_synopsis_data = self.change_object(row)
            command_synopsis_datas.append(command_synopsis_data)
        return command_synopsis_datas

    def change_object(self, row):
        if row == None:
            return None
        return CommandSynopsisVo(row)

    ######################################################################
    # select
    def count_commandsynopsis(self, command_id):
        where_string = f"command_id = {command_id}"
        return self.select_count(where_string)

    def select_commandsynopsis_all(self):
        rows = self.select_all()
        return self.change_object_list(rows)

    def select_commandsynopsis_list_by_is_require(self, command_id):
        where_string = "command_id = {} and is_require = 1".format(command_id)
        rows = self.select_where(where_string)
        return self.change_object_list(rows)

    def select_commandsynopsis_one_by_is_require(self, command_id):
        where_string = "command_id = {} and is_require = 1".format(command_id)
        row = self.select_one(where_string)
        return self.change_object(row)


    def select_commandsynopsis_list_by_is_option(self, command_id):
        where_string = "command_id = {} and is_require = 0".format(command_id)
        rows = self.select_where(where_string)
        return self.change_object_list(rows)

    def select_commandsynopsis_one_by_is_option(self, command_id, option_name):
        where_string = "command_id = {} and is_require = 0 and name like '{}%'".format(command_id, option_name)
        row = self.select_one(where_string)
        return self.change_object(row)
    ######################################################################
    # insert
    def insert_command_synopsis(self, command_id, name, value_name, is_require, service_name, command_name):
        now = datetime.now()
        replace_name = name.replace("'", "''")
        if is_require == True:
            require_num = 1
        else:
            require_num = 0

        value_string = "'{}', {}, '{}', '{}', {}, '', '{}', '', '{}', '{}'".format(replace_name, require_num, now, now, command_id, value_name, service_name, command_name)
        return self.insert_data("name, is_require, created_at, updated_at, command_id, comment, value_name, option_name, service_name, command_name", value_string)

    ######################################################################
    # update
    def update_command_synopsis_trim_name(self, id, trim_name):
        set_data = "trim_name = '" + trim_name + "'"
        where_string = "id = %d" % (id, )
        self.__update_data(set_data, where_string)

    def update_command_synopsis_comment(self, command_id, name, comment, option_name):
        replace_comment = comment.replace("'", "''")
        set_data = "comment = '" + replace_comment + "', option_name = '" + option_name + "'"
        where_string = "command_id = {} and name = '{}'".format(command_id, name)
        self.__update_data(set_data, where_string)

