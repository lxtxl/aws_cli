#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operations.html
if __name__ == '__main__':
    """
	describe-stack-set-operation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html
	stop-stack-set-operation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/stop-stack-set-operation.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set that you want to get operation summaries for.
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

    execute_one_parameter("cloudformation", "list-stack-set-operations", "stack-set-name", add_option_dict)