#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html
if __name__ == '__main__':
    """
	create-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html
	get-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html
	update-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("guardduty", "list-detectors", add_option_dict)