#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-classification-job.html
if __name__ == '__main__':
    """
	create-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-classification-job.html
	describe-classification-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/describe-classification-job.html
	list-classification-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-classification-jobs.html
    """

    parameter_display_string = """
    # job-id : The unique identifier for the classification job.
    # job-status : The new status for the job. Valid values are:

CANCELLED - Stops the job permanently and cancels it. You canât resume a job after you cancel it. This value is valid only if the jobâs current status is IDLE, PAUSED, RUNNING, or USER_PAUSED.
RUNNING - Resumes the job. This value is valid only if the jobâs current status is USER_PAUSED. If you specify this value, Amazon Macie immediately resumes the job.
USER_PAUSED - Pauses the job. This value is valid only if the jobâs current status is IDLE or RUNNING. If you specify this value and the job is currently running, Macie immediately stops running the job. To resume a job after you pause it, change the jobâs status to RUNNING. If you donât resume a job within 30 days of pausing it, the job expires and Macie cancels it. You canât resume a job after itâs cancelled.

Possible values:

RUNNING
PAUSED
CANCELLED
COMPLETE
IDLE
USER_PAUSED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("macie2", "update-classification-job", "job-id", "job-status", add_option_dict)
