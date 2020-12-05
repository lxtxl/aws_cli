#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-member-detectors.html
if __name__ == '__main__':
    """
	update-member-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-member-detectors.html
    """

    parameter_display_string = """
    # detector-id : The detector ID for the master account.
    # account-ids : The account ID of the member account.
(string)
    """

    execute_two_parameter("guardduty", "get-member-detectors", "detector-id", "account-ids", parameter_display_string)