#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/test-alarm.html
if __name__ == '__main__':
    """
	delete-alarm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-alarm.html
	get-alarms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-alarms.html
	put-alarm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-alarm.html
    """

    parameter_display_string = """
    # alarm-name : The name of the alarm to test.
    # state : The alarm state to test.
An alarm has the following possible states that can be tested:

ALARM - The metric is outside of the defined threshold.
INSUFFICIENT_DATA - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.
OK - The metric is within the defined threshold.

Possible values:

OK
ALARM
INSUFFICIENT_DATA
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "test-alarm", "alarm-name", "state", add_option_dict)
