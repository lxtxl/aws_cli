#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/delete-token.html
if __name__ == '__main__':
    """
	create-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-token.html
	get-token : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/get-token.html
    """

    parameter_display_string = """
    # app-id : The app ID.
    # session-id : The session ID.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("amplifybackend", "delete-token", "app-id", "session-id", add_option_dict)
