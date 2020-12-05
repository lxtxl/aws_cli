#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).
    # tags : The tags to be assigned to the Amazon DynamoDB resource.
(structure)

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a single DynamoDB table.
AWS-assigned tag names and values are automatically assigned the aws: prefix, which the user cannot assign. AWS-assigned tag names do not count towards the tag limit of 50. User-assigned tag names have the prefix user: in the Cost Allocation Report. You cannot backdate the application of a tag.
For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide .
Key -> (string)

The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.

Value -> (string)

The value of the tag. Tag values are case-sensitive and can be null.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "tag-resource", "resource-arn", "tags", add_option_dict)
