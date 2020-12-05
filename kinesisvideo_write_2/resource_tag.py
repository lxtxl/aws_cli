#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the signaling channel to which you want to add tags.
    # tags : A list of tags to associate with the specified signaling channel. Each tag is a key-value pair.
(structure)

A key and value pair that is associated with the specified signaling channel.
Key -> (string)

The key of the tag that is associated with the specified signaling channel.

Value -> (string)

The value of the tag that is associated with the specified signaling channel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesisvideo", "tag-resource", "resource-arn", "tags", add_option_dict)
