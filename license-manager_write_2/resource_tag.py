#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/tag-resource.html
if __name__ == '__main__':
    """
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/untag-resource.html
    """

    parameter_display_string = """
    # resource-arn : Amazon Resource Name (ARN) of the license configuration.
    # tags : One or more tags.
(structure)

Details about a tag for a license configuration.
Key -> (string)

Tag key.

Value -> (string)

Tag value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("license-manager", "tag-resource", "resource-arn", "tags", add_option_dict)
