#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/list-table-columns.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook that contains the table whose columns are being retrieved.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table whose columns are being retrieved.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    """

    execute_two_parameter("honeycode", "list-table-columns", "workbook-id", "table-id", parameter_display_string)