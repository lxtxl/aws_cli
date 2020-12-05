#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-table.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-tables.html
	update-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-table.html
    """

    parameter_display_string = """
    # database-name : The name of the Timestream database.
    # table-name : The name of the Timestream table.
    """

    execute_two_parameter("timestream-write", "describe-table", "database-name", "table-name", parameter_display_string)