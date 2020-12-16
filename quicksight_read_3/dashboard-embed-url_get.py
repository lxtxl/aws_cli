#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/get-dashboard-embed-url.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that contains the dashboard that youâre embedding.
    # dashboard-id : The ID for the dashboard, also added to the IAM policy.
    """

    execute_two_parameter("quicksight", "get-dashboard-embed-url", "aws-account-id", "dashboard-id", parameter_display_string)