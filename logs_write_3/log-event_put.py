#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-log-events.html
if __name__ == '__main__':
    """
	filter-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/filter-log-events.html
	get-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # log-stream-name : The name of the log stream.
    # log-events : The log events.
(structure)

Represents a log event, which is a record of activity that was recorded by the application or resource being monitored.
timestamp -> (long)

The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

message -> (string)

The raw event message.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("logs", "put-log-events", "log-group-name", "log-stream-name", "log-events", add_option_dict)
