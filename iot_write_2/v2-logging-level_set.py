#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-level.html
if __name__ == '__main__':
    """
	delete-v2-logging-level : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html
	list-v2-logging-levels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html
    """

    parameter_display_string = """
    # log-target : 
    # log-level : The log level.
Possible values:

DEBUG
INFO
ERROR
WARN
DISABLED
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "set-v2-logging-level", "log-target", "log-level", add_option_dict)
