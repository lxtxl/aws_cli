#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html
if __name__ == '__main__':
    """
	get-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-deployment.html
	list-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-deployments.html
	start-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/start-deployment.html
    """

    parameter_display_string = """
    # application-id : The application ID.
    # environment-id : The environment ID.
    # deployment-number : The sequence number of the deployment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appconfig", "stop-deployment", "application-id", "environment-id", "deployment-number", add_option_dict)
