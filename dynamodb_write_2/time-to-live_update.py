#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-time-to-live.html
if __name__ == '__main__':
    """
	describe-time-to-live : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-time-to-live.html
    """

    parameter_display_string = """
    # table-name : The name of the table to be configured.
    # time-to-live-specification : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "update-time-to-live", "table-name", "time-to-live-specification", add_option_dict)
