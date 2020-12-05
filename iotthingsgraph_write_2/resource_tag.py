#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource whose tags are returned.
    # tags : A list of tags to add to the resource.>
(structure)

Metadata assigned to an AWS IoT Things Graph resource consisting of a key-value pair.
key -> (string)

The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.

value -> (string)

The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotthingsgraph", "tag-resource", "resource-arn", "tags", add_option_dict)
