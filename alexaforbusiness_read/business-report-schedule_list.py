#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-business-report-schedules.html
if __name__ == '__main__':
    """
	create-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-business-report-schedule.html
	delete-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-business-report-schedule.html
	update-business-report-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-business-report-schedule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("alexaforbusiness", "list-business-report-schedules", add_option_dict)