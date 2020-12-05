#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-log.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-name : The name of the container service for which to get a container log.
    # container-name : The name of the container that is either running or previously ran on the container service for which to return a log.
    """

    execute_two_parameter("lightsail", "get-container-log", "service-name", "container-name", parameter_display_string)