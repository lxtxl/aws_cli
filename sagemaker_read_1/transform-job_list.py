#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-transform-job.html
if __name__ == '__main__':
    """
	create-transform-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-transform-job.html
	list-transform-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-transform-jobs.html
	stop-transform-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-transform-job.html
    """

    parameter_display_string = """
    # transform-job-name : The name of the transform job that you want to view details of.
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

    execute_one_parameter("sagemaker", "describe-transform-job", "transform-job-name", add_option_dict)