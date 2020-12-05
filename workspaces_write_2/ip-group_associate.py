#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-ip-groups.html
if __name__ == '__main__':
    """
	create-ip-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-ip-group.html
	delete-ip-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-ip-group.html
	describe-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-ip-groups.html
	disassociate-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-ip-groups.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory.
    # group-ids : The identifiers of one or more IP access control groups.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "associate-ip-groups", "directory-id", "group-ids", add_option_dict)
