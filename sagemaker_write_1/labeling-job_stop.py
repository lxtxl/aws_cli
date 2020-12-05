#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-labeling-job.html
if __name__ == '__main__':
    """
	create-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-labeling-job.html
	describe-labeling-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-labeling-job.html
	list-labeling-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-labeling-jobs.html
    """

    parameter_display_string = """
    # labeling-job-name : The name of the labeling job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-labeling-job", "labeling-job-name", add_option_dict)





