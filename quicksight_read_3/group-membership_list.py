#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-group-memberships.html
if __name__ == '__main__':
    """
	create-group-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-group-membership.html
	delete-group-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-group-membership.html
    """

    parameter_display_string = """
    # group-name : The name of the group that you want to see a membership list of.
    # aws-account-id : The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    """

    execute_two_parameter("quicksight", "list-group-memberships", "group-name", "aws-account-id", parameter_display_string)