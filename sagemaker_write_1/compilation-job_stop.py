#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-compilation-job.html
if __name__ == '__main__':
    """
	create-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-compilation-job.html
	describe-compilation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-compilation-job.html
	list-compilation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-compilation-jobs.html
    """

    parameter_display_string = """
    # compilation-job-name : The name of the model compilation job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-compilation-job", "compilation-job-name", add_option_dict)





