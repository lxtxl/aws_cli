#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-hyper-parameter-tuning-job.html
if __name__ == '__main__':
    """
	describe-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-hyper-parameter-tuning-job.html
	list-hyper-parameter-tuning-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hyper-parameter-tuning-jobs.html
	stop-hyper-parameter-tuning-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-hyper-parameter-tuning-job.html
    """

    parameter_display_string = """
    # hyper-parameter-tuning-job-name : The name of the tuning job. This name is the prefix for the names of all training jobs that this tuning job launches. The name must be unique within the same AWS account and AWS Region. The name must have 1 to 32 characters. Valid characters are a-z, A-Z, 0-9, and : + = @ _ % - (hyphen). The name is not case sensitive.
    # hyper-parameter-tuning-job-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-hyper-parameter-tuning-job", "hyper-parameter-tuning-job-name", "hyper-parameter-tuning-job-config", add_option_dict)
