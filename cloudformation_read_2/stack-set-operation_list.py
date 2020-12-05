#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html
if __name__ == '__main__':
    """
	list-stack-set-operations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operations.html
	stop-stack-set-operation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/stop-stack-set-operation.html
    """

    parameter_display_string = """
    # stack-set-name : The name or the unique stack ID of the stack set for the stack operation.
    # operation-id : The unique ID of the stack set operation.
    """

    execute_two_parameter("cloudformation", "describe-stack-set-operation", "stack-set-name", "operation-id", parameter_display_string)