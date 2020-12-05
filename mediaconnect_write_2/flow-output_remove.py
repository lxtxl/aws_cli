#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-output.html
if __name__ == '__main__':
    """
	add-flow-outputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-outputs.html
	update-flow-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html
    """

    parameter_display_string = """
    # flow-arn : The flow that you want to remove an output from.
    # output-arn : The ARN of the output that you want to remove.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "remove-flow-output", "flow-arn", "output-arn", add_option_dict)