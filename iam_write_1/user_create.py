#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html
if __name__ == '__main__':
    """
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
	get-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	tag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
	untag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    parameter_display_string = """
    # user-name : The name of the user to create.
IAM user, group, role, and policy names must be unique within the account. Names are not distinguished by case. For example, you cannot create resources named both âMyResourceâ and âmyresourceâ.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "create-user", "user-name", add_option_dict)





