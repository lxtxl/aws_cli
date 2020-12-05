#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-generation-job.html
if __name__ == '__main__':
    """
	cancel-world-generation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-world-generation-job.html
	create-world-generation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-generation-job.html
	list-world-generation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-generation-jobs.html
    """

    parameter_display_string = """
    # job : The Amazon Resource Name (arn) of the world generation job to describe.
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

    execute_one_parameter("robomaker", "describe-world-generation-job", "job", add_option_dict)