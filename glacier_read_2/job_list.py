#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-jobs.html
if __name__ == '__main__':
    """
	describe-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-job.html
	initiate-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-job.html
    """

    parameter_display_string = """
    # account-id : The AccountId value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single â- â (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens (â-â) in the ID.
    # vault-name : The name of the vault.
    """

    execute_two_parameter("glacier", "list-jobs", "account-id", "vault-name", parameter_display_string)