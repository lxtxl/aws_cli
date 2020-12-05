#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-third-party-job-details.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The unique system-generated ID used for identifying the job.
    # client-token : The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.
    """

    execute_two_parameter("codepipeline", "get-third-party-job-details", "job-id", "client-token", parameter_display_string)