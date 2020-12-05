#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-users.html
if __name__ == '__main__':
    """
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-user.html
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-user.html
	register-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/register-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-user.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # namespace : The namespace. Currently, you should set this to default .
    """

    execute_two_parameter("quicksight", "list-users", "aws-account-id", "namespace", parameter_display_string)