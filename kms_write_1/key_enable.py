#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key.html
if __name__ == '__main__':
    """
	create-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html
	describe-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html
	disable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html
	list-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-keys.html
    """

    parameter_display_string = """
    # key-id : A unique identifier for the customer master key (CMK).
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("kms", "enable-key", "key-id", add_option_dict)





