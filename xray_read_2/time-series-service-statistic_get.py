#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-time-series-service-statistics.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # start-time : 
    # end-time : 
    """

    execute_two_parameter("xray", "get-time-series-service-statistics", "start-time", "end-time", parameter_display_string)