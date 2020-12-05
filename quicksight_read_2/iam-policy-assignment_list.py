#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-iam-policy-assignments.html
if __name__ == '__main__':
    """
	create-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-iam-policy-assignment.html
	delete-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-iam-policy-assignment.html
	describe-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-iam-policy-assignment.html
	update-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-iam-policy-assignment.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains these IAM policy assignments.
    # namespace : The namespace for the assignments.
    """

    execute_two_parameter("quicksight", "list-iam-policy-assignments", "aws-account-id", "namespace", parameter_display_string)