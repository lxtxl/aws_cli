#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-log-pattern.html
if __name__ == '__main__':
    """
	create-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-log-pattern.html
	describe-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-log-pattern.html
	list-log-patterns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-log-patterns.html
	update-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-log-pattern.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
    # pattern-set-name : The name of the log pattern set.
    # pattern-name : The name of the log pattern.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("application-insights", "delete-log-pattern", "resource-group-name", "pattern-set-name", "pattern-name", add_option_dict)
