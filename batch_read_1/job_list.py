#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html
if __name__ == '__main__':
    """
	cancel-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/cancel-job.html
	list-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html
	submit-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html
	terminate-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html
    """

    parameter_display_string = """
    # jobs : A list of up to 100 job IDs.
(string)
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

    execute_one_parameter("batch", "describe-jobs", "jobs", add_option_dict)