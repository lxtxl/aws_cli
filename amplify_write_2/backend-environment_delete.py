#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-backend-environment.html
if __name__ == '__main__':
    """
	create-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-backend-environment.html
	get-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-backend-environment.html
	list-backend-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-backend-environments.html
    """

    parameter_display_string = """
    # app-id : The unique ID of an Amplify app.
    # environment-name : The name of a backend environment of an Amplify app.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("amplify", "delete-backend-environment", "app-id", "environment-name", add_option_dict)
