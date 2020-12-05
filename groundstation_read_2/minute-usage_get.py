#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-minute-usage.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # month : The month being requested, with a value of 1-12.
    # year : The year being requested, in the format of YYYY.
    """

    execute_two_parameter("groundstation", "get-minute-usage", "month", "year", parameter_display_string)