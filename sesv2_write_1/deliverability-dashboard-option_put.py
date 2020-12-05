#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/put-deliverability-dashboard-option.html
if __name__ == '__main__':
    """
	get-deliverability-dashboard-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-deliverability-dashboard-options.html
    """

    parameter_display_string = """
    # dashboard-enabled | --no-dashboard-enabled : Specifies whether to enable the Deliverability dashboard. To enable the dashboard, set this value to true .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sesv2", "put-deliverability-dashboard-option", "dashboard-enabled | --no-dashboard-enabled", add_option_dict)





