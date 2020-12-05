#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-dashboard.html
if __name__ == '__main__':
    """
	create-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-dashboard.html
	describe-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-dashboards.html
	update-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-dashboard.html
    """

    parameter_display_string = """
    # dashboard-id : The ID of the dashboard to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "delete-dashboard", "dashboard-id", add_option_dict)





