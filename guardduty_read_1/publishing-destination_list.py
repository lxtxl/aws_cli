#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-publishing-destinations.html
if __name__ == '__main__':
    """
	create-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-publishing-destination.html
	delete-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-publishing-destination.html
	describe-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-publishing-destination.html
	update-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-publishing-destination.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector to retrieve publishing destinations for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("guardduty", "list-publishing-destinations", "detector-id", add_option_dict)