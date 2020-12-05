#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-processing-job.html
if __name__ == '__main__':
    """
	create-processing-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-processing-job.html
	describe-processing-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-processing-job.html
	list-processing-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-processing-jobs.html
    """

    parameter_display_string = """
    # processing-job-name : The name of the processing job to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-processing-job", "processing-job-name", add_option_dict)





