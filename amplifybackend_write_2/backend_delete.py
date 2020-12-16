#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-backend.html
if __name__ == '__main__':
    """
	clone-backend : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/clone-backend.html
	create-backend : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend.html
	get-backend : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # backend-environment-name : The name of the backend environment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("amplifybackend", "delete-backend", "app-id", "backend-environment-name", add_option_dict)
