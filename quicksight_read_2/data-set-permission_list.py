#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-data-set-permissions.html
if __name__ == '__main__':
    """
	update-data-set-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID.
    # data-set-id : The ID for the dataset that you want to create. This ID is unique per AWS Region for each AWS account.
    """

    execute_two_parameter("quicksight", "describe-data-set-permissions", "aws-account-id", "data-set-id", parameter_display_string)