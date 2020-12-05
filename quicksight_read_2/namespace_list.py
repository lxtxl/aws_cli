#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-namespace.html
if __name__ == '__main__':
    """
	create-namespace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-namespace.html
	delete-namespace : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-namespace.html
	list-namespaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-namespaces.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that contains the QuickSight namespace that you want to describe.
    # namespace : The namespace that you want to describe.
    """

    execute_two_parameter("quicksight", "describe-namespace", "aws-account-id", "namespace", parameter_display_string)