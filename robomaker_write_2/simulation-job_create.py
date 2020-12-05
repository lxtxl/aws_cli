#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-job.html
if __name__ == '__main__':
    """
	cancel-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job.html
	describe-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job.html
	list-simulation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-jobs.html
	restart-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/restart-simulation-job.html
    """

    parameter_display_string = """
    # max-job-duration-in-seconds : 
    # iam-role : The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("robomaker", "create-simulation-job", "max-job-duration-in-seconds", "iam-role", add_option_dict)
