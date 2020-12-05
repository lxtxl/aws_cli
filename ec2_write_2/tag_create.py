#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-tags.html
if __name__ == '__main__':
    """
	delete-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-tags.html
	describe-tags : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-tags.html
    """

    parameter_display_string = """
    # resources : The IDs of the resources, separated by spaces.
Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.
(string)
    # tags : The tags. The value parameter is required, but if you donât want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
(structure)

Describes a tag.
Key -> (string)

The key of the tag.
Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with aws: .

Value -> (string)

The value of the tag.
Constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-tags", "resources", "tags", add_option_dict)
