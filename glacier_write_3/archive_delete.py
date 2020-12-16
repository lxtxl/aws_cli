#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-archive.html
if __name__ == '__main__':
    """
	upload-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/upload-archive.html
    """

    parameter_display_string = """
    # account-id : The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single â- â (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (â-â) in the ID.
    # vault-name : The name of the vault.
    # archive-id : The ID of the archive to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glacier", "delete-archive", "account-id", "vault-name", "archive-id", add_option_dict)
