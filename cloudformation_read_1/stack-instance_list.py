#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instances.html
if __name__ == '__main__':
    """
	create-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html
	delete-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-instances.html
	describe-stack-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html
	update-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-instances.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set that you want to list stack instances for.
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

    execute_one_parameter("cloudformation", "list-stack-instances", "stack-set-name", add_option_dict)