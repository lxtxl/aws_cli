#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-compilation-jobs.html
if __name__ == '__main__':
    """
	create-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-compilation-job.html
	describe-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-compilation-job.html
	stop-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-compilation-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("sagemaker", "list-compilation-jobs", add_option_dict)