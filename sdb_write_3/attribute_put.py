#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/put-attributes.html
if __name__ == '__main__':
    """
	delete-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-attributes.html
	get-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/get-attributes.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain in which to perform the operation.
    # item-name : The name of the item.
    # attributes : Name -> (string)

The name of the replaceable attribute.

Value -> (string)

The value of the replaceable attribute.

Replace -> (boolean)

A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is false .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sdb", "put-attributes", "domain-name", "item-name", "attributes", add_option_dict)
