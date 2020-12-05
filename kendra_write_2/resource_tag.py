#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the index, FAQ, or data source to tag.
    # tags : A list of tag keys to add to the index, FAQ, or data source. If a tag already exists, the existing value is replaced with the new value.
(structure)

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.
Key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, or data source.

Value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "tag-resource", "resource-arn", "tags", add_option_dict)
