#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/untag-resource.html
    """

    parameter_display_string = """
    # arn : The ARN of the resource to which to add metadata tags. Required.
    # tags : The tags to be added to the specified resource. Do not provide system tags. Required.
(structure)

A key-value pair that can be associated with a resource.
Key -> (string)

The key of a tag. Tag keys are case-sensitive.

Value -> (string)

The value of a tag. Tag values are case sensitive and can be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "tag-resource", "arn", "tags", add_option_dict)
