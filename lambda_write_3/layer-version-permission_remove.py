#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-layer-version-permission.html
if __name__ == '__main__':
    """
	add-layer-version-permission : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-layer-version-permission.html
    """

    parameter_display_string = """
    # layer-name : The name or Amazon Resource Name (ARN) of the layer.
    # version-number : 
    # statement-id : The identifier that was specified when the statement was added.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("lambda", "remove-layer-version-permission", "layer-name", "version-number", "statement-id", add_option_dict)
