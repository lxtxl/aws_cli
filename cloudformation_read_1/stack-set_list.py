#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set.html
if __name__ == '__main__':
    """
	create-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html
	delete-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-set.html
	list-stack-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-sets.html
	update-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set whose description you want.
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

    execute_one_parameter("cloudformation", "describe-stack-set", "stack-set-name", add_option_dict)