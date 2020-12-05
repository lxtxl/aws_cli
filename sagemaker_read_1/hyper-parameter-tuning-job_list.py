#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-hyper-parameter-tuning-job.html
if __name__ == '__main__':
    """
	create-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-hyper-parameter-tuning-job.html
	list-hyper-parameter-tuning-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hyper-parameter-tuning-jobs.html
	stop-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-hyper-parameter-tuning-job.html
    """

    parameter_display_string = """
    # hyper-parameter-tuning-job-name : The name of the tuning job.
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

    execute_one_parameter("sagemaker", "describe-hyper-parameter-tuning-job", "hyper-parameter-tuning-job-name", add_option_dict)