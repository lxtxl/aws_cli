#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-vault-lock.html
if __name__ == '__main__':
    """
	abort-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-vault-lock.html
	complete-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-vault-lock.html
	get-vault-lock : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-lock.html
    """

    parameter_display_string = """
    # account-id : The AccountId value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single â- â (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens (â-â) in the ID.
    # vault-name : The name of the vault.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("glacier", "initiate-vault-lock", "account-id", "vault-name", add_option_dict)
