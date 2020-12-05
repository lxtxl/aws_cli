#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-runs.html
if __name__ == '__main__':
    """
	cancel-ml-task-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/cancel-ml-task-run.html
	get-ml-task-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-ml-task-run.html
    """

    parameter_display_string = """
    # transform-id : The unique identifier of the machine learning transform.
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

    execute_one_parameter("glue", "get-ml-task-runs", "transform-id", add_option_dict)