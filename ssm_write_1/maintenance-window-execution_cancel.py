#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-maintenance-window-execution.html
if __name__ == '__main__':
    """
	describe-maintenance-window-executions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-executions.html
	get-maintenance-window-execution : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html
    """

    parameter_display_string = """
    # window-execution-id : The ID of the maintenance window execution to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "cancel-maintenance-window-execution", "window-execution-id", add_option_dict)





