#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : Identifies the Timestream resource to which tags should be added. This value is an Amazon Resource Name (ARN).
    # tags : The tags to be assigned to the Timestream resource.
(structure)

A tag is a label that you assign to a Timestream database and/or table. Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize databases and/or tables, for example, by purpose, owner, or environment.
Key -> (string)

The key of the tag. Tag keys are case sensitive.

Value -> (string)

The value of the tag. Tag values are case-sensitive and can be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("timestream-write", "tag-resource", "resource-arn", "tags", add_option_dict)
