#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-database.html
if __name__ == '__main__':
    """
	list-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-databases.html
    """

    parameter_display_string = """
    # catalog-name : The name of the data catalog that contains the database to return.
    # database-name : The name of the database to return.
    """

    execute_two_parameter("athena", "get-database", "catalog-name", "database-name", parameter_display_string)