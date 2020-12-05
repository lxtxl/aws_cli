#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-auto-ml-job.html
if __name__ == '__main__':
    """
	create-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-auto-ml-job.html
	describe-auto-ml-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-auto-ml-job.html
	list-auto-ml-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-auto-ml-jobs.html
    """

    parameter_display_string = """
    # auto-ml-job-name : The name of the object you are requesting.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-auto-ml-job", "auto-ml-job-name", add_option_dict)





