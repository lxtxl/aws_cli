#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-publishing-destination.html
if __name__ == '__main__':
    """
	create-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-publishing-destination.html
	delete-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-publishing-destination.html
	describe-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-publishing-destination.html
	list-publishing-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-publishing-destinations.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector associated with the publishing destinations to update.
    # destination-id : The ID of the publishing destination to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "update-publishing-destination", "detector-id", "destination-id", add_option_dict)
