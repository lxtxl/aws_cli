#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-schedule.html
if __name__ == '__main__':
    """
	create-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-schedule.html
	delete-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-schedule.html
	list-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-schedules.html
	update-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-schedule.html
    """

    parameter_display_string = """
    # name : The name of the schedule to be described.
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

    execute_one_parameter("databrew", "describe-schedule", "name", add_option_dict)