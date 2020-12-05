#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource you want to add tags to.
    # tags : The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.

Note
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tagâs key is 128 characters, and the maximum length for a tagâs value is 256.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.
Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "add-tags-to-resource", "resource-arn", "tags", add_option_dict)
