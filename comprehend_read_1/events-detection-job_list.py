#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-events-detection-job.html
if __name__ == '__main__':
    """
	list-events-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-events-detection-jobs.html
	start-events-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-events-detection-job.html
	stop-events-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-events-detection-job.html
    """

    parameter_display_string = """
    # job-id : The identifier of the events detection job.
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

    execute_one_parameter("comprehend", "describe-events-detection-job", "job-id", add_option_dict)