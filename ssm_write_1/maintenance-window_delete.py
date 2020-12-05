#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-maintenance-window.html
if __name__ == '__main__':
    """
	create-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-maintenance-window.html
	describe-maintenance-windows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html
	get-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html
	update-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html
    """

    parameter_display_string = """
    # window-id : The ID of the maintenance window to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "delete-maintenance-window", "window-id", add_option_dict)





