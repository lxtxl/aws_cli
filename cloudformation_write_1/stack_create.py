#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html
if __name__ == '__main__':
    """
	delete-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack.html
	describe-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html
	list-stacks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stacks.html
	update-stack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html
    """

    parameter_display_string = """
    # stack-name : The name that is associated with the stack. The name must be unique in the Region in which you are creating the stack.

Note
A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudformation", "create-stack", "stack-name", add_option_dict)





