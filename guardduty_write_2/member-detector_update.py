#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-member-detectors.html
if __name__ == '__main__':
    """
	get-member-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-member-detectors.html
    """

    parameter_display_string = """
    # detector-id : The detector ID of the master account.
    # account-ids : A list of member account IDs to be updated.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "update-member-detectors", "detector-id", "account-ids", add_option_dict)
