#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html
if __name__ == '__main__':
    """
	delete-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-change-set.html
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html
	execute-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/execute-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-change-sets.html
    """

    parameter_display_string = """
    # stack-name : The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates the change set by comparing this stackâs information with the information that you submit, such as a modified template or different parameter input values.
    # change-set-name : The name of the change set. The name must be unique among all change sets that are associated with the specified stack.
A change set name can contain only alphanumeric, case sensitive characters and hyphens. It must start with an alphabetic character and cannot exceed 128 characters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "create-change-set", "stack-name", "change-set-name", add_option_dict)
