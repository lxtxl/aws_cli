#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-journey.html
if __name__ == '__main__':
    """
	delete-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-journey.html
	get-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-journey.html
	list-journeys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/list-journeys.html
	update-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-journey.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # write-journey-request : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint", "create-journey", "application-id", "write-journey-request", add_option_dict)
