#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-user-endpoints.html
if __name__ == '__main__':
    """
	get-user-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-user-endpoints.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # user-id : The unique identifier for the user.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint", "delete-user-endpoints", "application-id", "user-id", add_option_dict)
