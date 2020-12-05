#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/set-stack-policy.html
if __name__ == '__main__':
    """
	get-stack-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-stack-policy.html
    """

    parameter_display_string = """
    # stack-name : The name or unique stack ID that you want to associate a policy with.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudformation", "set-stack-policy", "stack-name", add_option_dict)





