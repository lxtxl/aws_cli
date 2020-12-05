#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-name : The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name .
    # tags : The tags to be assigned to the Amazon DocumentDB resource.
(structure)

Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.
Key -> (string)

The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with âaws:â or ârds:â. The string can contain only the set of Unicode letters, digits, white space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).

Value -> (string)

The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with âaws:â or ârds:â. The string can contain only the set of Unicode letters, digits, white space, â_â, â.â, â/â, â=â, â+â, â-â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("docdb", "add-tags-to-resource", "resource-name", "tags", add_option_dict)
