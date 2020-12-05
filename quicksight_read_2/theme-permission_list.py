#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme-permissions.html
if __name__ == '__main__':
    """
	update-theme-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the theme that youâre describing.
    # theme-id : The ID for the theme that you want to describe permissions for.
    """

    execute_two_parameter("quicksight", "describe-theme-permissions", "aws-account-id", "theme-id", parameter_display_string)