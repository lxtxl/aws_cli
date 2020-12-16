#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-user.html
if __name__ == '__main__':
    """
	describe-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-users.html
	register-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/register-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-user.html
    """

    parameter_display_string = """
    # user-name : The name of the user that you want to delete.
    # aws-account-id : The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # namespace : The namespace. Currently, you should set this to default .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "delete-user", "user-name", "aws-account-id", "namespace", add_option_dict)
