#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-client-properties.html
if __name__ == '__main__':
    """
	describe-client-properties : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-client-properties.html
    """

    parameter_display_string = """
    # resource-id : The resource identifiers, in the form of directory IDs.
    # client-properties : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "modify-client-properties", "resource-id", "client-properties", add_option_dict)
