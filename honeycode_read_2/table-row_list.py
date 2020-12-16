#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/list-table-rows.html
if __name__ == '__main__':
    """
	query-table-rows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/query-table-rows.html
    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook that contains the table whose rows are being retrieved.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table whose rows are being retrieved.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    """

    execute_two_parameter("honeycode", "list-table-rows", "workbook-id", "table-id", parameter_display_string)