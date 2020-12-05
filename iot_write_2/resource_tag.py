#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the resource.
    # tags : The new or modified tags for the resource.
(structure)

A set of key/value pairs that are used to manage the resource.
Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "tag-resource", "resource-arn", "tags", add_option_dict)
