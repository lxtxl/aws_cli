#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/get-screen-data.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook that contains the screen.
    # app-id : The ID of the app that contains the screem.
    """

    execute_two_parameter("honeycode", "get-screen-data", "workbook-id", "app-id", parameter_display_string)