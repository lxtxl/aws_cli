#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The ARN of a resource, such as a CodeDeploy application or deployment group.
    # tags : A list of tags that TagResource associates with a resource. The resource is identified by the ResourceArn input parameter.
(structure)

Information about a tag.
Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("deploy", "tag-resource", "resource-arn", "tags", add_option_dict)
