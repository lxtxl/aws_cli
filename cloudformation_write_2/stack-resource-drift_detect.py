#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-resource-drift.html
if __name__ == '__main__':
    """
	describe-stack-resource-drifts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource-drifts.html
    """

    parameter_display_string = """
    # stack-name : The name of the stack to which the resource belongs.
    # logical-resource-id : The logical name of the resource for which to return drift information.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudformation", "detect-stack-resource-drift", "stack-name", "logical-resource-id", add_option_dict)
