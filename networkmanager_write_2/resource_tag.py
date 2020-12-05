#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource.
    # tags : The tags to apply to the specified resource.
(structure)

Describes a tag.
Key -> (string)

The tag key.
Length Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.
Length Constraints: Maximum length of 256 characters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("networkmanager", "tag-resource", "resource-arn", "tags", add_option_dict)
