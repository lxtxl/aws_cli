#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-groups.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-group.html
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-group.html
	describe-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-group.html
	update-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-group.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # namespace : The namespace. Currently, you should set this to default .
    """

    execute_two_parameter("quicksight", "list-groups", "aws-account-id", "namespace", parameter_display_string)