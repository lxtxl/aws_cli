#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-executions.html
if __name__ == '__main__':
    """
	cancel-maintenance-window-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-maintenance-window-execution.html
	get-maintenance-window-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html
    """

    parameter_display_string = """
    # window-id : The ID of the maintenance window whose executions should be retrieved.
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

    execute_one_parameter("ssm", "describe-maintenance-window-executions", "window-id", add_option_dict)