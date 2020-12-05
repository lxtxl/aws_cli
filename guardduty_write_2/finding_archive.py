#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/archive-findings.html
if __name__ == '__main__':
    """
	get-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html
	list-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html
	unarchive-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/unarchive-findings.html
    """

    parameter_display_string = """
    # detector-id : The ID of the detector that specifies the GuardDuty service whose findings you want to archive.
    # finding-ids : The IDs of the findings that you want to archive.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("guardduty", "archive-findings", "detector-id", "finding-ids", add_option_dict)
