#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-export-jobs.html
if __name__ == '__main__':
    """
	cancel-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/cancel-mailbox-export-job.html
	describe-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-mailbox-export-job.html
	start-mailbox-export-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/start-mailbox-export-job.html
    """

    parameter_display_string = """
    # organization-id : The organization ID.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("workmail", "list-mailbox-export-jobs", "organization-id", add_option_dict)