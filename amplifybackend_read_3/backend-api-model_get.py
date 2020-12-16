#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-backend-api-models.html
if __name__ == '__main__':
    """
	generate-backend-api-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/generate-backend-api-models.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # backend-environment-name : The name of the backend environment.
    """

    execute_two_parameter("amplifybackend", "get-backend-api-models", "app-id", "backend-environment-name", parameter_display_string)