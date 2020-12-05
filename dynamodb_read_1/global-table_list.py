#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table.html
if __name__ == '__main__':
    """
	create-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html
	list-global-tables : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-global-tables.html
	update-global-table : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table.html
    """

    parameter_display_string = """
    # global-table-name : The name of the global table.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("dynamodb", "describe-global-table", "global-table-name", add_option_dict)