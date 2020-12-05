#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/start-monitoring-members.html
if __name__ == '__main__':
    """
	stop-monitoring-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/stop-monitoring-members.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector of the GuardDuty master account associated with the member accounts to monitor.
    # account-ids : A list of account IDs of the GuardDuty member accounts to start monitoring.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "start-monitoring-members", "detector-id", "account-ids", add_option_dict)
