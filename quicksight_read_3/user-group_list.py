#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-user-groups.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # user-name : The Amazon QuickSight user name that you want to list group memberships for.
    # aws-account-id : The AWS account ID that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    """

    execute_two_parameter("quicksight", "list-user-groups", "user-name", "aws-account-id", parameter_display_string)