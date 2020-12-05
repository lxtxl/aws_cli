#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-resources.html
if __name__ == '__main__':
    """
	describe-stack-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource.html
	describe-stack-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resources.html
    """

    parameter_display_string = """
    # stack-name : The name or the unique stack ID that is associated with the stack, which are not always interchangeable:

Running stacks: You can specify either the stackâs name or its unique stack ID.
Deleted stacks: You must specify the unique stack ID.

Default: There is no default value.
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

    execute_one_parameter("cloudformation", "list-stack-resources", "stack-name", add_option_dict)