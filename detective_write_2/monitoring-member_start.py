#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/start-monitoring-member.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # graph-arn : The ARN of the behavior graph.
    # account-id : The account ID of the member account to try to enable.
The account must be an invited member account with a status of ACCEPTED_BUT_DISABLED .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("detective", "start-monitoring-member", "graph-arn", "account-id", add_option_dict)
