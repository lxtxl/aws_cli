#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-job-tagging.html
if __name__ == '__main__':
    """
	delete-job-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-job-tagging.html
	put-job-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-job-tagging.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID associated with the S3 Batch Operations job.
    # job-id : The ID for the S3 Batch Operations job whose tags you want to retrieve.
    """

    execute_two_parameter("s3control", "get-job-tagging", "account-id", "job-id", parameter_display_string)