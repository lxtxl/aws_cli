#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend-auth.html
if __name__ == '__main__':
    """
	create-backend-auth : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-auth.html
	delete-backend-auth : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-backend-auth.html
	update-backend-auth : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/update-backend-auth.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # backend-environment-name : The name of the backend environment.
    """

    execute_two_parameter("amplifybackend", "get-backend-auth", "app-id", "backend-environment-name", parameter_display_string)