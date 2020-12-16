#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-multipart-upload.html
if __name__ == '__main__':
    """
	abort-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-multipart-upload.html
	initiate-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-multipart-upload.html
	list-multipart-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-multipart-uploads.html
    """

    parameter_display_string = """
    # account-id : The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single â- â (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (â-â) in the ID.
    # vault-name : The name of the vault.
    # upload-id : The upload ID of the multipart upload.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glacier", "complete-multipart-upload", "account-id", "vault-name", "upload-id", add_option_dict)
