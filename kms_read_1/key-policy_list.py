#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-key-policies.html
if __name__ == '__main__':
    """
	get-key-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html
	put-key-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/put-key-policy.html
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
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("kms", "list-key-policies", "key-id", add_option_dict)