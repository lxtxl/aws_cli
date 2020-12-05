#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html
if __name__ == '__main__':
    """
	create-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html
	get-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html
	list-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("guardduty", "update-detector", "detector-id", add_option_dict)





