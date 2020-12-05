#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table-version.html
if __name__ == '__main__':
    """
	delete-table-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table-version.html
	get-table-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table-versions.html
    """

    parameter_display_string = """
    # database-name : The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
    # table-name : The name of the table. For Hive compatibility, this name is entirely lowercase.
    """

    execute_two_parameter("glue", "get-table-version", "database-name", "table-name", parameter_display_string)