#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-group.html
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-group.html
	get-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-groups.html
    """

    parameter_display_string = """
    # group-name : The name of the group.
    # user-pool-id : The user pool ID for the user pool.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-idp", "update-group", "group-name", "user-pool-id", add_option_dict)
