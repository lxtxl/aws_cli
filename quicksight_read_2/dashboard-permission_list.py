#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard-permissions.html
if __name__ == '__main__':
    """
	update-dashboard-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-dashboard-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the dashboard that youâre describing permissions for.
    # dashboard-id : The ID for the dashboard, also added to the IAM policy.
    """

    execute_two_parameter("quicksight", "describe-dashboard-permissions", "aws-account-id", "dashboard-id", parameter_display_string)