#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-configuration-set-sending-enabled.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that you want to update.
    # enabled | --no-enabled : Describes whether email sending is enabled or disabled for the configuration set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "update-configuration-set-sending-enabled", "configuration-set-name", "enabled | --no-enabled", add_option_dict)
