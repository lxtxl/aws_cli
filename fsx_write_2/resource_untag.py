#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/untag-resource.html
if __name__ == '__main__':
    """
	tag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/tag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the Amazon FSx resource to untag.
    # tag-keys : A list of keys of tags on the resource to untag. In case the tag key doesnât exist, the call will still succeed to be idempotent.
(string)

A string of 1 to 128 characters that specifies the key for a tag. Tag keys must be unique for the resource to which they are attached.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fsx", "untag-resource", "resource-arn", "tag-keys", add_option_dict)
