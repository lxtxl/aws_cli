#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/cancel-job.html
	describe-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html
	terminate-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html
    """

    parameter_display_string = """
    # job-name : The name of the job. The first character must be alphanumeric, and up to 128 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
    # job-queue : The job queue into which the job is submitted. You can specify either the name or the Amazon Resource Name (ARN) of the queue.
    # job-definition : The job definition used by this job. This value can be one of name , name:revision , or the Amazon Resource Name (ARN) for the job definition. If name is specified without a revision then the latest active revision is used.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("batch", "submit-job", "job-name", "job-queue", "job-definition", add_option_dict)
