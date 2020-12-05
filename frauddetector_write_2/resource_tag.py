#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The resource ARN.
    # tags : The tags to assign to the resource.
(structure)

A key and value pair.
key -> (string)

A tag key.

value -> (string)

A value assigned to a tag key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "tag-resource", "resource-arn", "tags", add_option_dict)
