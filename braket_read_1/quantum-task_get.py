#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-quantum-task.html
if __name__ == '__main__':
    """
	cancel-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/cancel-quantum-task.html
	create-quantum-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/create-quantum-task.html
	search-quantum-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/search-quantum-tasks.html
    """

    parameter_display_string = """
    # quantum-task-arn : the ARN of the task to retrieve.
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

    execute_one_parameter("braket", "get-quantum-task", "quantum-task-arn", add_option_dict)