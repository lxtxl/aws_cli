#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html
if __name__ == '__main__':
    """
	create-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html
	disable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html
	enable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key.html
	list-keys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-keys.html
    """

    parameter_display_string = """
    # key-id : Describes the specified customer master key (CMK).
If you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the alias with an AWS managed CMK and returns its KeyId and Arn in the response.
To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/" . To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.
For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
Alias name: alias/ExampleAlias
Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias

To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .
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

    execute_one_parameter("kms", "describe-key", "key-id", add_option_dict)