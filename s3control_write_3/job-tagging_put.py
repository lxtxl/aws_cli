#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-job-tagging.html
if __name__ == '__main__':
    """
	delete-job-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-job-tagging.html
	get-job-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-job-tagging.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID associated with the S3 Batch Operations job.
    # job-id : The ID for the S3 Batch Operations job whose tags you want to replace.
    # tags : The set of tags to associate with the S3 Batch Operations job.
(structure)

Key -> (string)
Value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "put-job-tagging", "account-id", "job-id", "tags", add_option_dict)
