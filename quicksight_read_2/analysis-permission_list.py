#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-analysis-permissions.html
if __name__ == '__main__':
    """
	update-analysis-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-analysis-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the analysis whose permissions youâre describing. You must be using the AWS account that the analysis is in.
    # analysis-id : The ID of the analysis whose permissions youâre describing. The ID is part of the analysis URL.
    """

    execute_two_parameter("quicksight", "describe-analysis-permissions", "aws-account-id", "analysis-id", parameter_display_string)