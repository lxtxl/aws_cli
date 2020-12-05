#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/get-devices-in-placement.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # project-name : The name of the project containing the placement.
    # placement-name : The name of the placement to get the devices from.
    """

    execute_two_parameter("iot1click-projects", "get-devices-in-placement", "project-name", "placement-name", parameter_display_string)