#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-monitoring-schedules.html
if __name__ == '__main__':
    """
	create-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-monitoring-schedule.html
	delete-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-monitoring-schedule.html
	describe-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-monitoring-schedule.html
	start-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-monitoring-schedule.html
	stop-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-monitoring-schedule.html
	update-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-monitoring-schedule.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("sagemaker", "list-monitoring-schedules", add_option_dict)