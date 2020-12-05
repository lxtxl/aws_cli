#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-account-settings.html
if __name__ == '__main__':
    """
	describe-account-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-account-settings.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that contains the QuickSight settings that you want to list.
    # default-namespace : The default namespace for this AWS account. Currently, the default is default . AWS Identity and Access Management (IAM) users that register for the first time with QuickSight provide an email that becomes associated with the default namespace.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-account-settings", "aws-account-id", "default-namespace", add_option_dict)
