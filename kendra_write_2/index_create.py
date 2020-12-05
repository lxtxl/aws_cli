#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html
if __name__ == '__main__':
    """
	delete-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-index.html
	describe-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-index.html
	update-index : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-index.html
    """

    parameter_display_string = """
    # name : The name for the new index.
    # role-arn : An AWS Identity and Access Management (IAM) role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics. This is also the role used when you use the BatchPutDocument operation to index documents from an Amazon S3 bucket.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "create-index", "name", "role-arn", add_option_dict)
