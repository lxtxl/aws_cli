#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-delete-table.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The name of the catalog database in which the tables to delete reside. For Hive compatibility, this name is entirely lowercase.
    # tables-to-delete : A list of the table to delete.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glue", "batch-delete-table", "database-name", "tables-to-delete", add_option_dict)
