#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/cancel-mailbox-export-job.html
if __name__ == '__main__':
    """
	describe-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-mailbox-export-job.html
	list-mailbox-export-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-export-jobs.html
	start-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/start-mailbox-export-job.html
    """

    parameter_display_string = """
    # job-id : The job ID.
    # organization-id : The organization ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("workmail", "cancel-mailbox-export-job", "job-id", "organization-id", add_option_dict)
