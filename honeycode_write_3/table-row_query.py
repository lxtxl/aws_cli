#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/query-table-rows.html
if __name__ == '__main__':
    """
	list-table-rows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/list-table-rows.html
    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook whose table rows are being queried.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table whose rows are being queried.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    # filter-formula : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("honeycode", "query-table-rows", "workbook-id", "table-id", "filter-formula", add_option_dict)
