#!/usr/bin/env python
import os
import sys
from .base_database import BaseDatabase
import logging

class VersionDatabase(BaseDatabase):
    TABLE_NAME = "VERSION"

    def __init__(self):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __init__(self, filename):
        logging.basicConfig(filename='logging.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        super().__init__(filename)

    def create(self):
        self.create_table(self.TABLE_NAME, "name varchar (512) NOT NULL")

    def insert_version_not_exist(self, version_info):
        if self.exist_version_data():
            self.logger.info("{} existed".format(version_info))
            return self.update_version_data(version_info)
        return self.insert_version_data(version_info)

    def select_version_one(self):
        column_string = "name"
        rows = self.select_all(self.TABLE_NAME, column_string)

        row = rows[0]

        return row[0]

    def exist_version_data(self):
        return self.exist_data(self.TABLE_NAME)

    def update_version_data(self, version_info):
        set_data = "name = '%s'" % (version_info, )
        self.update_data_all("aws_version", set_data)

    def insert_version_data(self, version_info):
        value_string = "'%s'" % (version_info, )
        return self.insert_data(self.TABLE_NAME, "name", value_string)