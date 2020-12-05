#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-import-job.html
if __name__ == '__main__':
    """
	create-import-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-import-job.html
	get-import-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-import-jobs.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # job-id : The unique identifier for the job.
    """

    execute_two_parameter("pinpoint", "get-import-job", "application-id", "job-id", parameter_display_string)