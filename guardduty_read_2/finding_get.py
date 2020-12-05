#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html
if __name__ == '__main__':
    """
	archive-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/archive-findings.html
	list-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html
	unarchive-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/unarchive-findings.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.
    # finding-ids : The IDs of the findings that you want to retrieve.
(string)
    """

    execute_two_parameter("guardduty", "get-findings", "detector-id", "finding-ids", parameter_display_string)