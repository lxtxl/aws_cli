#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/set-cognito-events.html
if __name__ == '__main__':
    """
	get-cognito-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-sync/get-cognito-events.html
    """

    parameter_display_string = """
    # identity-pool-id : The Cognito Identity Pool to use when configuring Cognito Events
    # events : The events to configure
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cognito-sync", "set-cognito-events", "identity-pool-id", "events", add_option_dict)
