#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-devices/list-device-events.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # device-id : The unique identifier of the device.
    # from-time-stamp : 
    """

    execute_two_parameter("iot1click-devices", "list-device-events", "device-id", "from-time-stamp", parameter_display_string)