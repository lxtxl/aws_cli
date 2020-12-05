#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/revoke-grant.html
if __name__ == '__main__':
    """
	create-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-grant.html
	list-grants : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-grants.html
	retire-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/retire-grant.html
    """

    parameter_display_string = """
    # key-id : A unique identifier for the customer master key associated with the grant.
Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # grant-id : Identifier of the grant to be revoked.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kms", "revoke-grant", "key-id", "grant-id", add_option_dict)
