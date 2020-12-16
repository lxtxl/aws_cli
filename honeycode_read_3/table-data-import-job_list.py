#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/describe-table-data-import-job.html
if __name__ == '__main__':
    """
	start-table-data-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/start-table-data-import-job.html
    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook into which data was imported.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table into which data was imported.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    """

    execute_two_parameter("honeycode", "describe-table-data-import-job", "workbook-id", "table-id", parameter_display_string)