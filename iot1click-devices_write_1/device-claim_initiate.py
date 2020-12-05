#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-devices/initiate-device-claim.html
if __name__ == '__main__':
    """
	finalize-device-claim : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-devices/finalize-device-claim.html
    """

    parameter_display_string = """
    # device-id : The unique identifier of the device.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot1click-devices", "initiate-device-claim", "device-id", add_option_dict)





