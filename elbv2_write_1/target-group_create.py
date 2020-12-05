#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html
if __name__ == '__main__':
    """
	delete-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-target-group.html
	describe-target-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-groups.html
	modify-target-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html
    """

    parameter_display_string = """
    # name : The name of the target group.
This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elbv2", "create-target-group", "name", add_option_dict)





