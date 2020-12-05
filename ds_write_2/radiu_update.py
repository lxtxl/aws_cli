#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/update-radius.html
if __name__ == '__main__':
    """
	disable-radius : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/disable-radius.html
	enable-radius : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/enable-radius.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory for which to update the RADIUS server information.
    # radius-settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ds", "update-radius", "directory-id", "radius-settings", add_option_dict)
