#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-alarm.html
if __name__ == '__main__':
    """
	get-alarms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-alarms.html
	put-alarm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-alarm.html
	test-alarm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/test-alarm.html
    """

    parameter_display_string = """
    # alarm-name : The name of the alarm to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "delete-alarm", "alarm-name", add_option_dict)





