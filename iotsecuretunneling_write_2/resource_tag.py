#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the resource.
    # tags : The tags for the resource.
(structure)

An arbitary key/value pair used to add searchable metadata to secure tunnel resources.
key -> (string)

The key of the tag.

value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsecuretunneling", "tag-resource", "resource-arn", "tags", add_option_dict)
