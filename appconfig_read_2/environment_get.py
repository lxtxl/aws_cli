#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-environment.html
if __name__ == '__main__':
    """
	create-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-environment.html
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-environment.html
    """

    parameter_display_string = """
    # application-id : The ID of the application that includes the environment you want to get.
    # environment-id : The ID of the environment you wnat to get.
    """

    execute_two_parameter("appconfig", "get-environment", "application-id", "environment-id", parameter_display_string)