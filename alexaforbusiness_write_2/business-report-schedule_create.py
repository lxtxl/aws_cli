#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-business-report-schedule.html
if __name__ == '__main__':
    """
	delete-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-business-report-schedule.html
	list-business-report-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-business-report-schedules.html
	update-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-business-report-schedule.html
    """

    parameter_display_string = """
    # format : The format of the generated report (individual CSV files or zipped files of individual files).
Possible values:

CSV
CSV_ZIP
    # content-range : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("alexaforbusiness", "create-business-report-schedule", "format", "content-range", add_option_dict)
