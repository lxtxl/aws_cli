#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-tags.html
if __name__ == '__main__':
    """
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-tags.html
	remove-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-tags.html
    """

    parameter_display_string = """
    # resource-arns : The Amazon Resource Name (ARN) of the resource.
(string)
    # tags : The tags.
(structure)

Information about a tag.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "add-tags", "resource-arns", "tags", add_option_dict)
