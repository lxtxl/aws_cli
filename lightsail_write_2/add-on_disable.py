#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/disable-add-on.html
if __name__ == '__main__':
    """
	enable-add-on : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/enable-add-on.html
    """

    parameter_display_string = """
    # add-on-type : The add-on type to disable.
Possible values:

AutoSnapshot
    # resource-name : The name of the source resource for which to disable the add-on.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "disable-add-on", "add-on-type", "resource-name", add_option_dict)
