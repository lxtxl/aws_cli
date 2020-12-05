#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-analysis-permissions.html
if __name__ == '__main__':
    """
	describe-analysis-permissions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-analysis-permissions.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the analysis whose permissions youâre updating. You must be using the AWS account that the analysis is in.
    # analysis-id : The ID of the analysis whose permissions youâre updating. The ID is part of the analysis URL.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("quicksight", "update-analysis-permissions", "aws-account-id", "analysis-id", add_option_dict)
