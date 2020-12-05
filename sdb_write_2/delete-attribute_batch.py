#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/batch-delete-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain-name : The name of the domain in which the attributes are being deleted.
    # items : Name -> (string)
Attributes -> (list)

(structure)

Name -> (string)

The name of the attribute.

AlternateNameEncoding -> (string)
Value -> (string)

The value of the attribute.

AlternateValueEncoding -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sdb", "batch-delete-attributes", "domain-name", "items", add_option_dict)
