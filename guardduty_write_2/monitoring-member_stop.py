#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/stop-monitoring-members.html
if __name__ == '__main__':
    """
	start-monitoring-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/start-monitoring-members.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector associated with the GuardDuty master account that is monitoring member accounts.
    # account-ids : A list of account IDs for the member accounts to stop monitoring.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "stop-monitoring-members", "detector-id", "account-ids", add_option_dict)
