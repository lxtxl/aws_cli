#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-users.html
    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the user exists.
    # user-id : The identifier for the user to be described.
    """

    execute_two_parameter("workmail", "describe-user", "organization-id", "user-id", parameter_display_string)