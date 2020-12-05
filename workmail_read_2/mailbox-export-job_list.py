#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-mailbox-export-job.html
if __name__ == '__main__':
    """
	cancel-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/cancel-mailbox-export-job.html
	list-mailbox-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-export-jobs.html
	start-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/start-mailbox-export-job.html
    """

    parameter_display_string = """
    # job-id : The mailbox export job ID.
    # organization-id : The organization ID.
    """

    execute_two_parameter("workmail", "describe-mailbox-export-job", "job-id", "organization-id", parameter_display_string)