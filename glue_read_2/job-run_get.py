#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-run.html
if __name__ == '__main__':
    """
	get-job-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-runs.html
	start-job-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-job-run.html
    """

    parameter_display_string = """
    # job-name : Name of the job definition being run.
    # run-id : The ID of the job run.
    """

    execute_two_parameter("glue", "get-job-run", "job-name", "run-id", parameter_display_string)