#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-subscription-filter.html
if __name__ == '__main__':
    """
	describe-subscription-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-subscription-filters.html
	put-subscription-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-subscription-filter.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # filter-name : The name of the subscription filter.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "delete-subscription-filter", "log-group-name", "filter-name", add_option_dict)
