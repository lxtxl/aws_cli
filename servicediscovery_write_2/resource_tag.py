#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.
    # tags : The tags to add to the specified resource. Specifying the tag key is required. You can set the value of a tag to an empty string, but you canât set the value of a tag to null.
(structure)

A custom key-value pair associated with a resource.
Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value associated with the key of the tag. You can set the value of a tag to an empty string, but you canât set the value of a tag to null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicediscovery", "tag-resource", "resource-arn", "tags", add_option_dict)
