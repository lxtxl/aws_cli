#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/restart-simulation-job.html
if __name__ == '__main__':
    """
	cancel-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job.html
	create-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-job.html
	describe-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job.html
	list-simulation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-jobs.html
    """

    parameter_display_string = """
    # job : The Amazon Resource Name (ARN) of the simulation job.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "restart-simulation-job", "job", add_option_dict)





