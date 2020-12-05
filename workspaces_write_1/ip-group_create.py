#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-ip-group.html
if __name__ == '__main__':
    """
	associate-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/associate-ip-groups.html
	delete-ip-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-ip-group.html
	describe-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-ip-groups.html
	disassociate-ip-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/disassociate-ip-groups.html
    """

    parameter_display_string = """
    # group-name : The name of the group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workspaces", "create-ip-group", "group-name", add_option_dict)





