#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/tag-resource.html
if __name__ == '__main__':
    """
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resources.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/untag-resource.html
    """

    parameter_display_string = """
    # resource-share-arn : The Amazon Resource Name (ARN) of the resource share.
    # tags : One or more tags.
(structure)

Information about a tag.
key -> (string)

The key of the tag.

value -> (string)

The value of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ram", "tag-resource", "resource-share-arn", "tags", add_option_dict)
