#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/set-alarm-state.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # alarm-name : The name of the alarm.
    # state-value : The value of the state.
Possible values:

OK
ALARM
INSUFFICIENT_DATA
    # state-reason : The reason that this alarm is set to this specific state, in text format.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudwatch", "set-alarm-state", "alarm-name", "state-value", "state-reason", add_option_dict)
