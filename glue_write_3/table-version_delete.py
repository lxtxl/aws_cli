#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table-version.html
if __name__ == '__main__':
    """
	get-table-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table-version.html
	get-table-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table-versions.html
    """

    parameter_display_string = """
    # database-name : The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
    # table-name : The name of the table. For Hive compatibility, this name is entirely lowercase.
    # version-id : The ID of the table version to be deleted. A VersionID is a string representation of an integer. Each version is incremented by 1.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "delete-table-version", "database-name", "table-name", "version-id", add_option_dict)
