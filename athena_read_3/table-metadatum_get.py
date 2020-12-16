#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html
if __name__ == '__main__':
    """
	list-table-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-table-metadata.html
    """

    parameter_display_string = """
    # catalog-name : The name of the data catalog that contains the database and table metadata to return.
    # database-name : The name of the database that contains the table metadata to return.
    """

    execute_two_parameter("athena", "get-table-metadata", "catalog-name", "database-name", parameter_display_string)