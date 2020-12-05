#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/enable-add-on.html
if __name__ == '__main__':
    """
	disable-add-on : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/disable-add-on.html
    """

    parameter_display_string = """
    # resource-name : The name of the source resource for which to enable or modify the add-on.
    # add-on-request : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "enable-add-on", "resource-name", "add-on-request", add_option_dict)
