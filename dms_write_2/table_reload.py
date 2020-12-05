#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reload-tables.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # replication-task-arn : The Amazon Resource Name (ARN) of the replication task.
    # tables-to-reload : The name and schema of the table to be reloaded.
(structure)

Provides the name of the schema and table to be reloaded.
SchemaName -> (string)

The schema name of the table to be reloaded.

TableName -> (string)

The table name of the table to be reloaded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "reload-tables", "replication-task-arn", "tables-to-reload", add_option_dict)
