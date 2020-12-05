#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.
    # tags : The tags you want to modify or add to the resource.
(structure)

A tag is a key-value pair that can be used to manage, search for, or filter resources in AWS CodeArtifact.
key -> (string)

The tagâs key.

value -> (string)

The tagâs value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeartifact", "tag-resource", "resource-arn", "tags", add_option_dict)
