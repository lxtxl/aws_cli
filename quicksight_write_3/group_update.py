#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-group.html
if __name__ == '__main__':
    """
	create-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-group.html
	delete-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-group.html
	describe-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-group.html
	list-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-groups.html
    """

    parameter_display_string = """
    # group-name : The name of the group that you want to update.
    # aws-account-id : The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.
    # namespace : The namespace. Currently, you should set this to default .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "update-group", "group-name", "aws-account-id", "namespace", add_option_dict)
