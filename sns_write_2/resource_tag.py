#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the topic to which to add tags.
    # tags : The tags to be added to the specified topic. A tag consists of a required key and an optional value.
(structure)

The list of tags to be added to the specified topic.
Key -> (string)

The required key portion of the tag.

Value -> (string)

The optional value portion of the tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sns", "tag-resource", "resource-arn", "tags", add_option_dict)
