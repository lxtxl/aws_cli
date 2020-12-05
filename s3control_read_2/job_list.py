#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html
if __name__ == '__main__':
    """
	create-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-jobs.html
    """

    parameter_display_string = """
    # account-id : The account ID for the AWS account whose PublicAccessBlock configuration you want to remove.
    # job-id : The ID for the job whose information you want to retrieve.
    """

    execute_two_parameter("s3control", "describe-job", "account-id", "job-id", parameter_display_string)