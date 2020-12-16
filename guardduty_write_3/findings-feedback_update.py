#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-findings-feedback.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # detector-id : The ID of the detector associated with the findings to update feedback for.
    # finding-ids : The IDs of the findings that you want to mark as useful or not useful.
(string)
    # feedback : The feedback for the finding.
Possible values:

USEFUL
NOT_USEFUL
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("guardduty", "update-findings-feedback", "detector-id", "finding-ids", "feedback", add_option_dict)
