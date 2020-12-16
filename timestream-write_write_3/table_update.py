#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-table.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/delete-table.html
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/describe-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/list-tables.html
    """

    parameter_display_string = """
    # database-name : The name of the Timestream database.
    # table-name : The name of the Timesream table.
    # retention-properties : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("timestream-write", "update-table", "database-name", "table-name", "retention-properties", add_option_dict)
