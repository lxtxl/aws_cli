#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-endpoint.html
if __name__ == '__main__':
    """
	delete-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-endpoint.html
	get-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-endpoint.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # endpoint-id : The unique identifier for the endpoint.
    # endpoint-request : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("pinpoint", "update-endpoint", "application-id", "endpoint-id", "endpoint-request", add_option_dict)
