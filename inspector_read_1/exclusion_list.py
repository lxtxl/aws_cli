#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-exclusions.html
if __name__ == '__main__':
    """
	list-exclusions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-exclusions.html
    """

    parameter_display_string = """
    # exclusion-arns : The list of ARNs that specify the exclusions that you want to describe.
(string)
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

    execute_one_parameter("inspector", "describe-exclusions", "exclusion-arns", add_option_dict)