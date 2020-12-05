#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-stream.html
if __name__ == '__main__':
    """
	create-log-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html
	describe-log-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-streams.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # log-stream-name : The name of the log stream.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "delete-log-stream", "log-group-name", "log-stream-name", add_option_dict)
