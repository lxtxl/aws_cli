#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-transform-job.html
if __name__ == '__main__':
    """
	create-transform-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-transform-job.html
	describe-transform-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-transform-job.html
	list-transform-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-transform-jobs.html
    """

    parameter_display_string = """
    # transform-job-name : The name of the transform job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-transform-job", "transform-job-name", add_option_dict)





