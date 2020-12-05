#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-journey.html
if __name__ == '__main__':
    """
	create-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-journey.html
	delete-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-journey.html
	list-journeys : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/list-journeys.html
	update-journey : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-journey.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # journey-id : The unique identifier for the journey.
    """

    execute_two_parameter("pinpoint", "get-journey", "application-id", "journey-id", parameter_display_string)