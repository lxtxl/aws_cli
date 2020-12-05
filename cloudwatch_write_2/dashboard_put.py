#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-dashboard.html
if __name__ == '__main__':
    """
	delete-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-dashboards.html
	get-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-dashboards.html
    """

    parameter_display_string = """
    # dashboard-name : The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, â-â, and â_â. This parameter is required.
    # dashboard-body : The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.
For more information about the syntax, see Dashboard Body Structure and Syntax .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudwatch", "put-dashboard", "dashboard-name", "dashboard-body", add_option_dict)
