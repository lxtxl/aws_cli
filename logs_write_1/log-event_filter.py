#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/filter-log-events.html
if __name__ == '__main__':
    """
	get-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-log-events.html
	put-log-events : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-log-events.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group to search.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("logs", "filter-log-events", "log-group-name", add_option_dict)





