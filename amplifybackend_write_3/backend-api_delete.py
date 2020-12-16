#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-backend-api.html
if __name__ == '__main__':
    """
	create-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-api.html
	get-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend-api.html
	update-backend-api : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/update-backend-api.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # backend-environment-name : The name of the backend environment.
    # resource-name : The name of this resource.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("amplifybackend", "delete-backend-api", "app-id", "backend-environment-name", "resource-name", add_option_dict)
