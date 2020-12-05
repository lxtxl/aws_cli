#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-publishing-destination.html
if __name__ == '__main__':
    """
	create-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-publishing-destination.html
	delete-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-publishing-destination.html
	list-publishing-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-publishing-destinations.html
	update-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-publishing-destination.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector associated with the publishing destination to retrieve.
    # destination-id : The ID of the publishing destination to retrieve.
    """

    execute_two_parameter("guardduty", "describe-publishing-destination", "detector-id", "destination-id", parameter_display_string)