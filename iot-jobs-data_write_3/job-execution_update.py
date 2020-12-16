#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html
if __name__ == '__main__':
    """
	describe-job-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/describe-job-execution.html
    """

    parameter_display_string = """
    # job-id : The unique identifier assigned to this job when it was created.
    # thing-name : The name of the thing associated with the device.
    # status : The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.
Possible values:

QUEUED
IN_PROGRESS
SUCCEEDED
FAILED
TIMED_OUT
REJECTED
REMOVED
CANCELED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot-jobs-data", "update-job-execution", "job-id", "thing-name", "status", add_option_dict)
