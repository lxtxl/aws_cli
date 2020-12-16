#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-delete-table-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # database-name : The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
    # table-name : The name of the table. For Hive compatibility, this name is entirely lowercase.
    # version-ids : A list of the IDs of versions to be deleted. A VersionId is a string representation of an integer. Each version is incremented by 1.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "batch-delete-table-version", "database-name", "table-name", "version-ids", add_option_dict)
