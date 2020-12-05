#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-backend-environment.html
if __name__ == '__main__':
    """
	create-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-backend-environment.html
	delete-backend-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-backend-environment.html
	list-backend-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-backend-environments.html
    """

    parameter_display_string = """
    # app-id : The unique id for an Amplify app.
    # environment-name : The name for the backend environment.
    """

    execute_two_parameter("amplify", "get-backend-environment", "app-id", "environment-name", parameter_display_string)