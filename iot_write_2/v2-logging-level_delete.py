#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html
if __name__ == '__main__':
    """
	list-v2-logging-levels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html
	set-v2-logging-level : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-level.html
    """

    parameter_display_string = """
    # target-type : The type of resource for which you are configuring logging. Must be THING_Group .
Possible values:

DEFAULT
THING_GROUP
    # target-name : The name of the resource for which you are configuring logging.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iot", "delete-v2-logging-level", "target-type", "target-name", add_option_dict)
