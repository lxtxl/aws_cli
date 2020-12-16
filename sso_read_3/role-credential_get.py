#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/get-role-credentials.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # role-name : The friendly name of the role that is assigned to the user.
    # account-id : The identifier for the AWS account that is assigned to the user.
    """

    execute_two_parameter("sso", "get-role-credentials", "role-name", "account-id", parameter_display_string)