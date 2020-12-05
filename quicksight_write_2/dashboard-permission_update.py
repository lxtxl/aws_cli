#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-dashboard-permissions.html
if __name__ == '__main__':
    """
	describe-dashboard-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the dashboard whose permissions youâre updating.
    # dashboard-id : The ID for the dashboard.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-dashboard-permissions", "aws-account-id", "dashboard-id", add_option_dict)
