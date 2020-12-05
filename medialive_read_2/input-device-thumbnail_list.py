#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-input-device-thumbnail.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # input-device-id : The unique ID of this input device. For example, hd-123456789abcdef.
    # accept : Possible values:

image/jpeg
    """

    execute_two_parameter("medialive", "describe-input-device-thumbnail", "input-device-id", "accept", parameter_display_string)