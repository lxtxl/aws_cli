#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html
if __name__ == '__main__':
    """
	delete-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-dashboards.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-dashboards.html
	put-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-dashboard.html
    """

    parameter_display_string = """
    # dashboard-name : The name of the dashboard to be described.
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

    execute_one_parameter("cloudwatch", "get-dashboard", "dashboard-name", add_option_dict)