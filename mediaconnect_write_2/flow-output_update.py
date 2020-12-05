#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html
if __name__ == '__main__':
    """
	add-flow-outputs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-outputs.html
	remove-flow-output : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-output.html
    """

    parameter_display_string = """
    # flow-arn : The flow that is associated with the output that you want to update.
    # output-arn : The ARN of the output that you want to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mediaconnect", "update-flow-output", "flow-arn", "output-arn", add_option_dict)
