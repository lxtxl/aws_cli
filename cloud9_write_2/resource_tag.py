#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Name (ARN) of the AWS Cloud9 development environment to add tags to.
    # tags : The list of tags to add to the given AWS Cloud9 development environment.
(structure)

Metadata that is associated with AWS resources. In particular, a name-value pair that can be associated with an AWS Cloud9 development environment. There are two types of tags: user tags and system tags . A user tag is created by the user. A system tag is automatically created by AWS services. A system tag is prefixed with âaws:â and cannot be modified by the user.
Key -> (string)

The name part of a tag.

Value -> (string)

The value part of a tag.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloud9", "tag-resource", "resource-arn", "tags", add_option_dict)
