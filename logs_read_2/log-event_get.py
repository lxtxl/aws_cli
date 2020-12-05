#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html
if __name__ == '__main__':
    """
	filter-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/filter-log-events.html
	put-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-log-events.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # log-stream-name : The name of the log stream.
    """

    execute_two_parameter("logs", "get-log-events", "log-group-name", "log-stream-name", parameter_display_string)