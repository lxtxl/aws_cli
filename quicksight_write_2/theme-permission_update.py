#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme-permissions.html
if __name__ == '__main__':
    """
	describe-theme-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the theme.
    # theme-id : The ID for the theme.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-theme-permissions", "aws-account-id", "theme-id", add_option_dict)
