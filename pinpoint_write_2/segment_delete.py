#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-segment.html
if __name__ == '__main__':
    """
	create-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-segment.html
	get-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-segment.html
	get-segments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-segments.html
	update-segment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-segment.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # segment-id : The unique identifier for the segment.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint", "delete-segment", "application-id", "segment-id", add_option_dict)
