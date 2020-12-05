#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/revoke-ip-rules.html
if __name__ == '__main__':
    """
	authorize-ip-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/authorize-ip-rules.html
    """

    parameter_display_string = """
    # group-id : The identifier of the group.
    # user-rules : The rules to remove from the group.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "revoke-ip-rules", "group-id", "user-rules", add_option_dict)
