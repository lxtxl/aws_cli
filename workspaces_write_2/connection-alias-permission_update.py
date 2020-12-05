#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/update-connection-alias-permission.html
if __name__ == '__main__':
    """
	describe-connection-alias-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-connection-alias-permissions.html
    """

    parameter_display_string = """
    # alias-id : The identifier of the connection alias that you want to update permissions for.
    # connection-alias-permission : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "update-connection-alias-permission", "alias-id", "connection-alias-permission", add_option_dict)
