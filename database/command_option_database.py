import os
import sys
from .base_database import BaseDatabase
import logging
from datetime import datetime

class CommandOptionDatabase(BaseDatabase):
    TABLE_NAME = "COMMAND_OPTION"

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
        field_list.append("comment varchar(1024) NOT NULL")
        field_list.append("created_at datetime NOT NULL")
        field_list.append("updated_at datetime NOT NULL")
        field_list.append("command_id integer NOT NULL REFERENCES \"COMMAND\"(\"id\") DEFERRABLE INITIALLY DEFERRED")
        field = ",".join(field_list)
        self.create_table(self.TABLE_NAME, field)


    def insert_command_option(self, command_id, name, comment):
        now = datetime.now()
        replace_name = name.replace("'", "''")
        replace_comment = comment.replace("'", "''")

        value_string = "'%s', '%s', '%s', '%s', %d" % (replace_name, replace_comment, now, now, command_id)
        return self.insert_data(self.TABLE_NAME, "name, comment, created_at, updated_at, command_id", value_string)
