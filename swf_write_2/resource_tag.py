#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) for the Amazon SWF domain.
    # tags : The list of tags to add to a domain.
Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
(structure)

Tags are key-value pairs that can be associated with Amazon SWF state machines and activities.
Tags may only contain unicode letters, digits, whitespace, or these symbols: _ . : / = + - @ .
key -> (string)

The key of a tag.

value -> (string)

The value of a tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "tag-resource", "resource-arn", "tags", add_option_dict)
