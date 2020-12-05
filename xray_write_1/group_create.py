#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/create-group.html
if __name__ == '__main__':
    """
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/delete-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-group.html
	get-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/update-group.html
    """

    parameter_display_string = """
    # group-name : The case-sensitive name of the new group. Default is a reserved name and names must be unique.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("xray", "create-group", "group-name", add_option_dict)





