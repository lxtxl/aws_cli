#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-user-by-principal-id.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # principal-id : The principal ID of the user.
    # aws-account-id : The ID for the AWS account that the user is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # namespace : The namespace. Currently, you should set this to default .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "delete-user-by-principal-id", "principal-id", "aws-account-id", "namespace", add_option_dict)
