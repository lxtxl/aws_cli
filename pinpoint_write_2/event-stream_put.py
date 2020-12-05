#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/put-event-stream.html
if __name__ == '__main__':
    """
	delete-event-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-event-stream.html
	get-event-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-event-stream.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # write-event-stream : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint", "put-event-stream", "application-id", "write-event-stream", add_option_dict)
