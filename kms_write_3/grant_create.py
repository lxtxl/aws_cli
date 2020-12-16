#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-grant.html
if __name__ == '__main__':
    """
	list-grants : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-grants.html
	retire-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/retire-grant.html
	revoke-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/revoke-grant.html
    """

    parameter_display_string = """
    # key-id : The unique identifier for the customer master key (CMK) that the grant applies to.
Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # grantee-principal : The principal that is given permission to perform the operations that the grant permits.
To specify the principal, use the Amazon Resource Name (ARN) of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see AWS Identity and Access Management (IAM) in the Example ARNs section of the AWS General Reference .
    # operations : A list of operations that the grant permits.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kms", "create-grant", "key-id", "grantee-principal", "operations", add_option_dict)
