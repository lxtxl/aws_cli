#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-monitoring-schedule.html
if __name__ == '__main__':
    """
	create-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-monitoring-schedule.html
	delete-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-monitoring-schedule.html
	describe-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-monitoring-schedule.html
	list-monitoring-schedules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-monitoring-schedules.html
	start-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-monitoring-schedule.html
	update-monitoring-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-monitoring-schedule.html
    """

    parameter_display_string = """
    # monitoring-schedule-name : The name of the schedule to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "stop-monitoring-schedule", "monitoring-schedule-name", add_option_dict)





