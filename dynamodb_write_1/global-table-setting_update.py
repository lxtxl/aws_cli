#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table-settings.html
if __name__ == '__main__':
    """
	describe-global-table-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table-settings.html
    """

    parameter_display_string = """
    # global-table-name : The name of the global table
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "update-global-table-settings", "global-table-name", add_option_dict)





