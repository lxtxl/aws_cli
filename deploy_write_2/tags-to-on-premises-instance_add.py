#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/add-tags-to-on-premises-instances.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # tags : The tag key-value pairs to add to the on-premises instances.
Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.
(structure)

Information about a tag.
Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.
    # instance-names : The names of the on-premises instances to which to add tags.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("deploy", "add-tags-to-on-premises-instances", "tags", "instance-names", add_option_dict)
