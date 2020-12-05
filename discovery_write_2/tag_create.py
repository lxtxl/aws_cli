#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/create-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/delete-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-tags.html
    """

    parameter_display_string = """
    # configuration-ids : A list of configuration items that you want to tag.
(string)
    # tags : Tags that you want to associate with one or more configuration items. Specify the tags that you want to create in a key -value format. For example:

{"key": "serverType", "value": "webServer"}

(structure)

Metadata that help you categorize IT assets.
key -> (string)

The type of tag on which to filter.

value -> (string)

A value for a tag key on which to filter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("discovery", "create-tags", "configuration-ids", "tags", add_option_dict)
