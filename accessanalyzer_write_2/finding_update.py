#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-findings.html
if __name__ == '__main__':
    """
	get-finding : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding.html
	list-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings.html
    """

    parameter_display_string = """
    # analyzer-arn : The ARN of the analyzer that generated the findings to update.
    # status : The state represents the action to take to update the finding Status. Use ARCHIVE to change an Active finding to an Archived finding. Use ACTIVE to change an Archived finding to an Active finding.
Possible values:

ACTIVE
ARCHIVED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("accessanalyzer", "update-findings", "analyzer-arn", "status", add_option_dict)
