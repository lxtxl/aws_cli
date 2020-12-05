#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-environment.html
if __name__ == '__main__':
    """
	create-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-environment.html
	get-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-environment.html
    """

    parameter_display_string = """
    # application-id : The application ID that includes the environment you want to delete.
    # environment-id : The ID of the environment you want to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("appconfig", "delete-environment", "application-id", "environment-id", add_option_dict)
