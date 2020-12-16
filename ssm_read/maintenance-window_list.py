#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html
if __name__ == '__main__':
    """
	create-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-maintenance-window.html
	delete-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-maintenance-window.html
	get-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html
	update-maintenance-window : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("ssm", "describe-maintenance-windows", add_option_dict)