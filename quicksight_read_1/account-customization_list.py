#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-account-customization.html
if __name__ == '__main__':
    """
	create-account-customization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-account-customization.html
	delete-account-customization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-account-customization.html
	update-account-customization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-account-customization.html
    """

    parameter_display_string = """
    # aws-account-id : The ID for the AWS account that you want to describe QuickSight customizations for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("quicksight", "describe-account-customization", "aws-account-id", add_option_dict)