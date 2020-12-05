#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-table.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-table.html
	get-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-tables.html
	search-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/search-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-table.html
    """

    parameter_display_string = """
    # database-name : The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.
    # name : The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.
    """

    execute_two_parameter("glue", "get-table", "database-name", "name", parameter_display_string)