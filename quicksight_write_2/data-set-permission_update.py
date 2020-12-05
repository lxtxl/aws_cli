#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set-permissions.html
if __name__ == '__main__':
    """
	describe-data-set-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-data-set-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The AWS account ID.
    # data-set-id : The ID for the dataset whose permissions you want to update. This ID is unique per AWS Region for each AWS account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-data-set-permissions", "aws-account-id", "data-set-id", add_option_dict)
