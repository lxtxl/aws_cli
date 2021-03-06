#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html
if __name__ == '__main__':
    """
	create-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html
	list-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stacks.html
    """

    parameter_display_string = """
    # stack-name : The name or unique stack ID of the stack to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudformation", "update-stack", "stack-name", add_option_dict)





