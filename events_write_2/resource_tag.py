#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of the EventBridge resource that youâre adding tags to.
    # tags : The list of key-value pairs to associate with the resource.
(structure)

A key-value pair associated with an AWS resource. In EventBridge, rules and event buses support tagging.
Key -> (string)

A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("events", "tag-resource", "resource-arn", "tags", add_option_dict)
