#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/describe-job-execution.html
if __name__ == '__main__':
    """
	update-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html
    """

    parameter_display_string = """
    # job-id : The unique identifier assigned to this job when it was created.
    # thing-name : The thing name associated with the device the job execution is running on.
    """

    execute_two_parameter("iot-jobs-data", "describe-job-execution", "job-id", "thing-name", parameter_display_string)