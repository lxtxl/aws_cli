#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-key-description.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # key-id : A unique identifier for the customer master key (CMK).
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # description : New description for the CMK.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kms", "update-key-description", "key-id", "description", add_option_dict)
