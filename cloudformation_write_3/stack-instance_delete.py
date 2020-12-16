#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-instances.html
if __name__ == '__main__':
    """
	create-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html
	describe-stack-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html
	list-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instances.html
	update-stack-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-instances.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set that you want to delete stack instances for.
    # regions : The Regions where you want to delete stack set instances.
(string)
    # retain-stacks | --no-retain-stacks : Removes the stack instances from the specified stack set, but doesnât delete the stacks. You canât reassociate a retained stack or add an existing, saved stack to a new stack set.
For more information, see Stack set operation options .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudformation", "delete-stack-instances", "stack-set-name", "regions", "retain-stacks | --no-retain-stacks", add_option_dict)
