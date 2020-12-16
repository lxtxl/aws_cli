#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/disassociate-device-from-placement.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # project-name : The name of the project that contains the placement.
    # placement-name : The name of the placement that the device should be removed from.
    # device-template-name : The device ID that should be removed from the placement.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iot1click-projects", "disassociate-device-from-placement", "project-name", "placement-name", "device-template-name", add_option_dict)
