#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the application to assign the tags.
    # tags : The key-value tags to assign to the application.
(structure)

A key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see Using Tagging .
Key -> (string)

The key of the key-value tag.

Value -> (string)

The value of the key-value tag. The value is optional.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesisanalyticsv2", "tag-resource", "resource-arn", "tags", add_option_dict)
