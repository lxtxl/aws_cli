#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.
    # tag-list : One or more tags.
(structure)

A key-value pair that identifies or specifies metadata about an AWS CloudHSM resource.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsm", "add-tags-to-resource", "resource-arn", "tag-list", add_option_dict)
