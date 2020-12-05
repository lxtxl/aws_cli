#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-log-patterns.html
if __name__ == '__main__':
    """
	create-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-log-pattern.html
	delete-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-log-pattern.html
	describe-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-log-pattern.html
	update-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-log-pattern.html
    """

    parameter_display_string = """
    # resource-group-name : The name of the resource group.
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

    execute_one_parameter("application-insights", "list-log-patterns", "resource-group-name", add_option_dict)