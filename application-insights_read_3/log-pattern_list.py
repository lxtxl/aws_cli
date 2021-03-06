#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-log-pattern.html
if __name__ == '__main__':
    """
	create-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-log-pattern.html
	delete-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-log-pattern.html
	list-log-patterns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-log-patterns.html
	update-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-log-pattern.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
    # pattern-set-name : The name of the log pattern set.
    """

    execute_two_parameter("application-insights", "describe-log-pattern", "resource-group-name", "pattern-set-name", parameter_display_string)