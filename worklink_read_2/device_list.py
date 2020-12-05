#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-device.html
if __name__ == '__main__':
    """
	list-devices : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-devices.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # device-id : A unique identifier for a registered userâs device.
    """

    execute_two_parameter("worklink", "describe-device", "fleet-arn", "device-id", parameter_display_string)