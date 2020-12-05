#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html
if __name__ == '__main__':
    """
	create-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html
	delete-snapshot-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-schedule.html
	describe-snapshot-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html
    """

    parameter_display_string = """
    # schedule-identifier : A unique alphanumeric identifier of the schedule to modify.
    # schedule-definitions : An updated list of schedule definitions. A schedule definition is made up of schedule expressions, for example, âcron(30 12 *)â or ârate(12 hours)â.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "modify-snapshot-schedule", "schedule-identifier", "schedule-definitions", add_option_dict)
