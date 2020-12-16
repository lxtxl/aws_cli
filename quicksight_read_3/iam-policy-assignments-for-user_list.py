#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-iam-policy-assignments-for-user.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the assignments.
    # user-name : The name of the user.
    """

    execute_two_parameter("quicksight", "list-iam-policy-assignments-for-user", "aws-account-id", "user-name", parameter_display_string)