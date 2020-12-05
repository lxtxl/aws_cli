#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/delete-dashboards.html
if __name__ == '__main__':
    """
	get-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/get-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/list-dashboards.html
	put-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-dashboard.html
    """

    parameter_display_string = """
    # dashboard-names : The dashboards to be deleted. This parameter is required.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudwatch", "delete-dashboards", "dashboard-names", add_option_dict)





