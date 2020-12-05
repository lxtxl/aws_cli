#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/notify-application-state.html
if __name__ == '__main__':
    """
	describe-application-state : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/describe-application-state.html
	list-application-states : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-application-states.html
    """

    parameter_display_string = """
    # application-id : The configurationId in Application Discovery Service that uniquely identifies the grouped application.
    # status : Status of the application - Not Started, In-Progress, Complete.
Possible values:

NOT_STARTED
IN_PROGRESS
COMPLETED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("mgh", "notify-application-state", "application-id", "status", add_option_dict)
