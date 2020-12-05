#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/untag-resource.html
    """

    parameter_display_string = """
    # resource-id : The ID specifying the EFS resource that you want to create a tag for.
    # tags : (structure)

A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:+ - = . _ : /
Key -> (string)

The tag key (String). The key canât start with aws: .

Value -> (string)

The value of the tag key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("efs", "tag-resource", "resource-id", "tags", add_option_dict)
