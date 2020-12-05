#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/add-tags-to-resource.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # resource-arn : Identifies the AWS DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).
For AWS DMS, you can tag a replication instance, an endpoint, or a replication task.
    # tags : One or more tags to be assigned to the resource.
(structure)

A user-defined key-value pair that describes metadata added to an AWS DMS resource and that is used by operations such as the following:

AddTagsToResource
ListTagsForResource
RemoveTagsFromResource

Key -> (string)

A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+-]*)$â).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "add-tags-to-resource", "resource-arn", "tags", add_option_dict)
