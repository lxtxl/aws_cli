#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-policy.html
if __name__ == '__main__':
    """
	list-key-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-key-policies.html
	put-key-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/put-key-policy.html
    """

    parameter_display_string = """
    # key-id : A unique identifier for the customer master key (CMK).
Specify the key ID or the Amazon Resource Name (ARN) of the CMK.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .
    # policy-name : Specifies the name of the key policy. The only valid name is default . To get the names of key policies, use  ListKeyPolicies .
    """

    execute_two_parameter("kms", "get-key-policy", "key-id", "policy-name", parameter_display_string)