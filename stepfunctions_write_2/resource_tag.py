#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) for the Step Functions state machine or activity.
    # tags : The list of tags to add to a resource.
Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .
(structure)

Tags are key-value pairs that can be associated with Step Functions state machines and activities.
An array of key-value pairs. For more information, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide , and Controlling Access Using IAM Tags .
Tags may only contain Unicode letters, digits, white space, or these symbols: _ . : / = + - @ .
key -> (string)

The key of a tag.

value -> (string)

The value of a tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("stepfunctions", "tag-resource", "resource-arn", "tags", add_option_dict)
