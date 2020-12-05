#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operation-results.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stack-set-name : The name or unique ID of the stack set that you want to get operation results for.
    # operation-id : The ID of the stack set operation.
    """

    execute_two_parameter("cloudformation", "list-stack-set-operation-results", "stack-set-name", "operation-id", parameter_display_string)