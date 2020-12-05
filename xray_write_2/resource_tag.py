#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.
    # tags : A map that contains one or more tag keys and tag values to attach to an X-Ray group or sampling rule. For more information about ways to use tags, see Tagging AWS resources in the AWS General Reference .
The following restrictions apply to tags:

Maximum number of user-applied tags per resource: 50
Maximum tag key length: 128 Unicode characters
Maximum tag value length: 256 Unicode characters
Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @
Tag keys and values are case sensitive.
Donât use aws: as a prefix for keys; itâs reserved for AWS use. You cannot edit or delete system tags.

(structure)

A map that contains tag keys and tag values to attach to an AWS X-Ray group or sampling rule. For more information about ways to use tags, see Tagging AWS resources in the AWS General Reference .
The following restrictions apply to tags:

Maximum number of user-applied tags per resource: 50
Tag keys and values are case sensitive.
Donât use aws: as a prefix for keys; itâs reserved for AWS use. You cannot edit or delete system tags.

Key -> (string)

A tag key, such as Stage or Name . A tag key cannot be empty. The key can be a maximum of 128 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /

Value -> (string)

An optional tag value, such as Production or test-only . The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: + - = . _ : /
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("xray", "tag-resource", "resource-arn", "tags", add_option_dict)
