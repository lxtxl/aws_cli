#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-auto-ml-job.html
if __name__ == '__main__':
    """
	create-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-auto-ml-job.html
	list-auto-ml-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-auto-ml-jobs.html
	stop-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-auto-ml-job.html
    """

    parameter_display_string = """
    # auto-ml-job-name : Request information about a job using that jobâs unique name.
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

    execute_one_parameter("sagemaker", "describe-auto-ml-job", "auto-ml-job-name", add_option_dict)