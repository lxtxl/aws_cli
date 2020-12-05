#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-stack-policy.html
if __name__ == '__main__':
    """
	set-stack-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/set-stack-policy.html
    """

    parameter_display_string = """
    # stack-name : The name or unique stack ID that is associated with the stack whose policy you want to get.
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

    execute_one_parameter("cloudformation", "get-stack-policy", "stack-name", add_option_dict)