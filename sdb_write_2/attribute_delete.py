#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-attributes.html
if __name__ == '__main__':
    """
	get-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/get-attributes.html
	put-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/put-attributes.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain in which to perform the operation.
    # item-name : The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sdb", "delete-attributes", "domain-name", "item-name", add_option_dict)
