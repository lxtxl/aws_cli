#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings.html
if __name__ == '__main__':
    """
	get-finding : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding.html
	update-findings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-findings.html
    """

    parameter_display_string = """
    # analyzer-arn : The ARN of the analyzer to retrieve findings from.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("accessanalyzer", "list-findings", "analyzer-arn", add_option_dict)