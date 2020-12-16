#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-dashboard.html
if __name__ == '__main__':
    """
	delete-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-dashboard.html
	describe-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-dashboards.html
	update-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-dashboard.html
    """

    parameter_display_string = """
    # project-id : The ID of the project in which to create the dashboard.
    # dashboard-name : A friendly name for the dashboard.
    # dashboard-definition : The dashboard definition specified in a JSON literal. For detailed information, see Creating dashboards (CLI) in the AWS IoT SiteWise User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iotsitewise", "create-dashboard", "project-id", "dashboard-name", "dashboard-definition", add_option_dict)
