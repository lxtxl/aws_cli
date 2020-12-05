#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users-in-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-pool-id : The user pool ID for the user pool.
    # group-name : The name of the group.
    """

    execute_two_parameter("cognito-idp", "list-users-in-group", "user-pool-id", "group-name", parameter_display_string)