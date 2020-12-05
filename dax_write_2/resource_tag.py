#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/untag-resource.html
    """

    parameter_display_string = """
    # resource-name : The name of the DAX resource to which tags should be added.
    # tags : The tags to be assigned to the DAX resource.
(structure)

A description of a tag. Every tag is a key-value pair. You can add up to 50 tags to a single DAX cluster.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: .
You cannot backdate the application of a tag.
Key -> (string)

The key for the tag. Tag keys are case sensitive. Every DAX cluster can only have one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value -> (string)

The value of the tag. Tag values are case-sensitive and can be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dax", "tag-resource", "resource-name", "tags", add_option_dict)
