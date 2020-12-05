#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-instances.html
if __name__ == '__main__':
    """
	create-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html
	delete-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-instances.html
	describe-stack-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html
	list-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instances.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set associated with the stack instances.
    # regions : The names of one or more Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Regions.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "update-stack-instances", "stack-set-name", "regions", add_option_dict)
