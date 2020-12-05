#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/describe-application-state.html
if __name__ == '__main__':
    """
	list-application-states : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-application-states.html
	notify-application-state : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/notify-application-state.html
    """

    parameter_display_string = """
    # application-id : The configurationId in Application Discovery Service that uniquely identifies the grouped application.
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

    execute_one_parameter("mgh", "describe-application-state", "application-id", add_option_dict)