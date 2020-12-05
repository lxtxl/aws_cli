#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html
if __name__ == '__main__':
    """
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-group.html
    """

    parameter_display_string = """
    # group-name : The name of the group to create. Do not include the path in this value.
IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both âMyResourceâ and âmyresourceâ.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "create-group", "group-name", add_option_dict)





