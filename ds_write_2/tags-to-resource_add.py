#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-id : Identifier (ID) for the directory to which to add the tag.
    # tags : The tags to be assigned to the directory.
(structure)

Metadata assigned to a directory consisting of a key-value pair.
Key -> (string)

Required name of the tag. The string value can be Unicode characters and cannot be prefixed with âaws:â. The string can contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).

Value -> (string)

The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "add-tags-to-resource", "resource-id", "tags", add_option_dict)
