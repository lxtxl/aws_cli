#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-topics-detection-job.html
if __name__ == '__main__':
    """
	list-topics-detection-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-topics-detection-jobs.html
	start-topics-detection-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-topics-detection-job.html
    """

    parameter_display_string = """
    # job-id : The identifier assigned by the user to the detection job.
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

    execute_one_parameter("comprehend", "describe-topics-detection-job", "job-id", add_option_dict)