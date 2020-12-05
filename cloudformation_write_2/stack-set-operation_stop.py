#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/stop-stack-set-operation.html
if __name__ == '__main__':
    """
	describe-stack-set-operation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html
	list-stack-set-operations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operations.html
    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set that you want to stop the operation for.
    # operation-id : The ID of the stack operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "stop-stack-set-operation", "stack-set-name", "operation-id", add_option_dict)
