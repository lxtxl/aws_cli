#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/search-insights.html
if __name__ == '__main__':
    """
	describe-insight : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/describe-insight.html
	list-insights : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-insights.html
    """

    parameter_display_string = """
    # start-time-range : 
    # type : Possible values:

REACTIVE
PROACTIVE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("devops-guru", "search-insights", "start-time-range", "type", add_option_dict)
