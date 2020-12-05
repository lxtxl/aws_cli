#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html
if __name__ == '__main__':
    """
	get-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html
	list-layer-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html
	publish-layer-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html
    """

    parameter_display_string = """
    # layer-name : The name or Amazon Resource Name (ARN) of the layer.
    # version-number : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lambda", "delete-layer-version", "layer-name", "version-number", add_option_dict)
