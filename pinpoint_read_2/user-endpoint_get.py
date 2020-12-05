#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-user-endpoints.html
if __name__ == '__main__':
    """
	delete-user-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-user-endpoints.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # user-id : The unique identifier for the user.
    """

    execute_two_parameter("pinpoint", "get-user-endpoints", "application-id", "user-id", parameter_display_string)