#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-iam-policy-assignment.html
if __name__ == '__main__':
    """
	create-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-iam-policy-assignment.html
	describe-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-iam-policy-assignment.html
	list-iam-policy-assignments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-iam-policy-assignments.html
	update-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-iam-policy-assignment.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID where you want to delete the IAM policy assignment.
    # assignment-name : The name of the assignment.
    # namespace : The namespace that contains the assignment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "delete-iam-policy-assignment", "aws-account-id", "assignment-name", "namespace", add_option_dict)
