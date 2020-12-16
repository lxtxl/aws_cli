#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-deployment.html
if __name__ == '__main__':
    """
	list-deployments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-deployments.html
	start-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/start-deployment.html
	stop-deployment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html
    """

    parameter_display_string = """
    # application-id : The ID of the application that includes the deployment you want to get.
    # environment-id : The ID of the environment that includes the deployment you want to get.
    """

    execute_two_parameter("appconfig", "get-deployment", "application-id", "environment-id", parameter_display_string)