#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-jobs.html
if __name__ == '__main__':
    """
	cancel-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job.html
	create-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-simulation-job.html
	describe-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job.html
	restart-simulation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/restart-simulation-job.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("robomaker", "list-simulation-jobs", add_option_dict)