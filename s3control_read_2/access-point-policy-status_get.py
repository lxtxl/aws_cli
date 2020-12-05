#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-policy-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # account-id : The account ID for the account that owns the specified access point.
    # name : The name of the access point whose policy status you want to retrieve.
    """

    execute_two_parameter("s3control", "get-access-point-policy-status", "account-id", "name", parameter_display_string)