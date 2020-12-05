#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-group.html
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-groups.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-group.html
    """

    parameter_display_string = """
    # group-name : The name of the group.
    # user-pool-id : The user pool ID for the user pool.
    """

    execute_two_parameter("cognito-idp", "get-group", "group-name", "user-pool-id", parameter_display_string)