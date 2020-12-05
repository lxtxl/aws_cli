#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-dashboard.html
if __name__ == '__main__':
    """
	create-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-dashboard.html
	delete-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-dashboards.html
	update-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-dashboard.html
    """

    parameter_display_string = """
    # dashboard-id : The ID of the dashboard.
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

    execute_one_parameter("iotsitewise", "describe-dashboard", "dashboard-id", add_option_dict)