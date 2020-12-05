#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-business-report-schedule.html
if __name__ == '__main__':
    """
	create-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-business-report-schedule.html
	delete-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-business-report-schedule.html
	list-business-report-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-business-report-schedules.html
    """

    parameter_display_string = """
    # schedule-arn : The ARN of the business report schedule.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("alexaforbusiness", "update-business-report-schedule", "schedule-arn", add_option_dict)





