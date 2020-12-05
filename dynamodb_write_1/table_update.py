#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table.html
if __name__ == '__main__':
    """
	create-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-table.html
	delete-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html
	describe-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-table.html
	list-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tables.html
    """

    parameter_display_string = """
    # table-name : The name of the table to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "update-table", "table-name", add_option_dict)





