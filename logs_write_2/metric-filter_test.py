#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/test-metric-filter.html
if __name__ == '__main__':
    """
	delete-metric-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-metric-filter.html
	describe-metric-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-metric-filters.html
	put-metric-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-metric-filter.html
    """

    parameter_display_string = """
    # filter-pattern : A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.
    # log-event-messages : The log event messages to test.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "test-metric-filter", "filter-pattern", "log-event-messages", add_option_dict)
