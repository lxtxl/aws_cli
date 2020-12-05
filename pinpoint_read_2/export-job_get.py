#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-export-job.html
if __name__ == '__main__':
    """
	create-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-export-job.html
	get-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-export-jobs.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # job-id : The unique identifier for the job.
    """

    execute_two_parameter("pinpoint", "get-export-job", "application-id", "job-id", parameter_display_string)