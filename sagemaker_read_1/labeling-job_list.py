#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-labeling-job.html
if __name__ == '__main__':
    """
	create-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-labeling-job.html
	list-labeling-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-labeling-jobs.html
	stop-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-labeling-job.html
    """

    parameter_display_string = """
    # labeling-job-name : The name of the labeling job to return information for.
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

    execute_one_parameter("sagemaker", "describe-labeling-job", "labeling-job-name", add_option_dict)