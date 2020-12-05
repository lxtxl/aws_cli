#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN ) that is assigned to and uniquely identifies the GameLift resource that you want to assign tags to. GameLift resource ARNs are included in the data object for the resource, which can be retrieved by calling a List or Describe operation for the resource type.
    # tags : A list of one or more tags to assign to the specified GameLift resource. Tags are developer-defined and structured as key-value pairs. The maximum tag limit may be lower than stated. See Tagging AWS Resources for actual tagging limits.
(structure)

A label that can be assigned to a GameLift resource.

Learn more
Tagging AWS Resources in the AWS General Reference
AWS Tagging Strategies
Related operations


TagResource
UntagResource
ListTagsForResource

Key -> (string)

The key for a developer-defined key:value pair for tagging an AWS resource.

Value -> (string)

The value for a developer-defined key:value pair for tagging an AWS resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("gamelift", "tag-resource", "resource-arn", "tags", add_option_dict)
