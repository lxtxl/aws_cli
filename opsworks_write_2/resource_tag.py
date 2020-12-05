#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The stack or layerâs Amazon Resource Number (ARN).
    # tags : A map that contains tag keys and tag values that are attached to a stack or layer.

The key cannot be empty.
The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /
The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /
Leading and trailing white spaces are trimmed from both the key and value.
A maximum of 40 tags is allowed for any resource.

key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "tag-resource", "resource-arn", "tags", add_option_dict)
