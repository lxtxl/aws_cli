#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/search-devices.html
if __name__ == '__main__':
    """
	get-device : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-device.html
    """

    parameter_display_string = """
    # filters : The filter values to use to search for a device.
(structure)

The filter to use for searching devices.
name -> (string)

The name to use to filter results.

values -> (list)

The values to use to filter results.
(string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("braket", "search-devices", "filters", add_option_dict)





