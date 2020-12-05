#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-tags.html
    """

    parameter_display_string = """
    # resource-id : The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.
    # tags : The tags. Each WorkSpaces resource can have a maximum of 50 tags.
(structure)

Describes a tag.
Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workspaces", "create-tags", "resource-id", "tags", add_option_dict)
