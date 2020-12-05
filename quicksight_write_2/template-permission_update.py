#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template-permissions.html
if __name__ == '__main__':
    """
	describe-template-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the template.
    # template-id : The ID for the template.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-template-permissions", "aws-account-id", "template-id", add_option_dict)
