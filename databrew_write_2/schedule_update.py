#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-schedule.html
if __name__ == '__main__':
    """
	create-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-schedule.html
	delete-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/delete-schedule.html
	describe-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-schedule.html
	list-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-schedules.html
    """

    parameter_display_string = """
    # cron-expression : The date or dates and time or times, in cron format, when the jobs are to be run.
    # name : The name of the schedule to update.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "update-schedule", "cron-expression", "name", add_option_dict)
