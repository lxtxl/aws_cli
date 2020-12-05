#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/authorize-ip-rules.html
if __name__ == '__main__':
    """
	revoke-ip-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/revoke-ip-rules.html
    """

    parameter_display_string = """
    # group-id : The identifier of the group.
    # user-rules : The rules to add to the group.
(structure)

Describes a rule for an IP access control group.
ipRule -> (string)

The IP address range, in CIDR notation.

ruleDesc -> (string)

The description.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "authorize-ip-rules", "group-id", "user-rules", add_option_dict)
