#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-table-metadata.html
if __name__ == '__main__':
    """
	get-table-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html
    """

    parameter_display_string = """
    # catalog-name : The name of the data catalog for which table metadata should be returned.
    # database-name : The name of the database for which table metadata should be returned.
    """

    execute_two_parameter("athena", "list-table-metadata", "catalog-name", "database-name", parameter_display_string)