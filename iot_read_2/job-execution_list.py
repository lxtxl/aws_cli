#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-execution.html
if __name__ == '__main__':
    """
	cancel-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job-execution.html
	delete-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job-execution.html
    """

    parameter_display_string = """
    # job-id : The unique identifier you assigned to this job when it was created.
    # thing-name : The name of the thing on which the job execution is running.
    """

    execute_two_parameter("iot", "describe-job-execution", "job-id", "thing-name", parameter_display_string)