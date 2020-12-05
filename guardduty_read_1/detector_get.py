#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html
if __name__ == '__main__':
    """
	create-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html
	list-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html
	update-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that you want to get.
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

    execute_one_parameter("guardduty", "get-detector", "detector-id", add_option_dict)