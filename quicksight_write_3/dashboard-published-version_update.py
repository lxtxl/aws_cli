#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-dashboard-published-version.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the dashboard that youâre updating.
    # dashboard-id : The ID for the dashboard.
    # version-number : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("quicksight", "update-dashboard-published-version", "aws-account-id", "dashboard-id", "version-number", add_option_dict)
