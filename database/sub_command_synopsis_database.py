import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import date, datetime
from .sub_command_synopsis_vo import SubCommandSynopsisVo


class SubCommandSynopsisDatabase(BaseDatabase):
    TABLE_NAME="SUB_COMMAND_SYNOPSIS"

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
        field_list.append("value_name varchar(300) NOT NULL")
        field_list.append("option_name varchar(300) NOT NULL")
        field_list.append("is_require bool NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("comment text NOT NULL")
        field_list.append("sub_command_id integer NOT NULL REFERENCES SUB_COMMAND (id) DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)

    ######################################################################
    # common
    def __select_where(self, where_string):
        return self.select_common_where(self.TABLE_NAME, SubCommandSynopsisVo.get_select_query(), where_string)

    def __select_distinct_where(self, value_string, where_string):
        return self.select_common_distinct_where(self.TABLE_NAME, value_string, where_string)

    def __select_all(self):
        return self.select_common_all(self.TABLE_NAME, SubCommandSynopsisVo.get_select_query())

    def __select_one(self, where_string):
        return self.select_common_one(self.TABLE_NAME, SubCommandSynopsisVo.get_select_query(), where_string)

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
        if row is None:
            return None
        return SubCommandSynopsisVo(row)

    ######################################################################
    # select
    def count_commandsynopsis(self, command_id):
        where_string = f"command_id = {command_id}"
        return self.__select_count(where_string)

    def select_commandsynopsis_all(self):
        rows = self.__select_all()
        return self.__change_object_list(rows)

    def select_commandsynopsis_list_by_is_require(self, command_id):
        where_string = "command_id = {} and is_require = 1".format(command_id)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_commandsynopsis_list_by_is_option(self, command_id):
        where_string = "command_id = {} and is_require = 0".format(command_id)
        rows = self.__select_where(where_string)
        return self.__change_object_list(rows)

    def select_commandsynopsis_one_by_is_option(self, command_id, option_name):
        where_string = "command_id = {} and is_require = 0 and name like '{}%'".format(command_id, option_name)
        row = self.__select_one(where_string)
        return self.__change_object(row)
    ######################################################################
    # insert
    def insert_sub_command_synopsis(self, sub_command_id, name, value_name, is_require, service_name, command_name):
        now = datetime.now()
        replace_name = name.replace("'", "''")
        if is_require == True:
            require_num = 1
        else:
            require_num = 0

        value_string = "'{}', {}, '{}', '{}', {}, '', '{}', ''".format(replace_name, require_num, now, now, sub_command_id, value_name)
        return self.__insert_data("name, is_require, created_at, updated_at, sub_command_id, comment, value_name, option_name", value_string)

    ######################################################################
    # update
    def update_command_synopsis_trim_name(self, id, trim_name):
        set_data = "trim_name = '" + trim_name + "'"
        where_string = "id = %d" % (id, )
        self.__update_data(set_data, where_string)

    def update_sub_command_synopsis_comment(self, sub_command_id, name, comment, option_name):
        replace_comment = comment.replace("'", "''")
        set_data = "comment = '" + replace_comment + "', option_name = '" + option_name + "'"
        where_string = "sub_command_id = {} and name = '{}'".format(sub_command_id, name)
        self.__update_data(set_data, where_string)

