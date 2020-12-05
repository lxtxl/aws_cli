#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/remove-tags-from-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-name : The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).
    # tag-keys : The tag key (name) of the tag to be removed.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("docdb", "remove-tags-from-resource", "resource-name", "tag-keys", add_option_dict)
