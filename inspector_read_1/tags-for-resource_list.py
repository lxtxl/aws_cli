#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-tags-for-resource.html
if __name__ == '__main__':
    """
	set-tags-for-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/set-tags-for-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN that specifies the assessment template whose tags you want to list.
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

    execute_one_parameter("inspector", "list-tags-for-resource", "resource-arn", add_option_dict)