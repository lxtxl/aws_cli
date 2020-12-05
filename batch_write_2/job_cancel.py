#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/cancel-job.html
if __name__ == '__main__':
    """
	describe-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html
	submit-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html
	terminate-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html
    """

    parameter_display_string = """
    # job-id : The AWS Batch job ID of the job to cancel.
    # reason : A message to attach to the job that explains the reason for canceling it. This message is returned by future  DescribeJobs operations on the job. This message is also recorded in the AWS Batch activity logs.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("batch", "cancel-job", "job-id", "reason", add_option_dict)
