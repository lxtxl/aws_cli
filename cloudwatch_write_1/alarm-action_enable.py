#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/enable-alarm-actions.html
if __name__ == '__main__':
    """
	disable-alarm-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/disable-alarm-actions.html
    """

    parameter_display_string = """
    # alarm-names : The names of the alarms.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudwatch", "enable-alarm-actions", "alarm-names", add_option_dict)





