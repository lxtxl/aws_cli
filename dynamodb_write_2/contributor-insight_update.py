#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-contributor-insights.html
if __name__ == '__main__':
    """
	describe-contributor-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-contributor-insights.html
	list-contributor-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-contributor-insights.html
    """

    parameter_display_string = """
    # table-name : The name of the table.
    # contributor-insights-action : Represents the contributor insights action.
Possible values:

ENABLE
DISABLE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "update-contributor-insights", "table-name", "contributor-insights-action", add_option_dict)
