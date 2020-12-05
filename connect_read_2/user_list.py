#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-users.html
    """

    parameter_display_string = """
    # user-id : The identifier of the user account.
    # instance-id : The identifier of the Amazon Connect instance.
    """

    execute_two_parameter("connect", "describe-user", "user-id", "instance-id", parameter_display_string)