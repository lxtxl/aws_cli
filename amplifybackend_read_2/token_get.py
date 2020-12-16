#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-token.html
if __name__ == '__main__':
    """
	create-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-token.html
	delete-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-token.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # session-id : The session ID.
    """

    execute_two_parameter("amplifybackend", "get-token", "app-id", "session-id", parameter_display_string)