#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-maintenance-start-time.html
if __name__ == '__main__':
    """
	describe-maintenance-start-time : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-maintenance-start-time.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # hour-of-day : The hour component of the maintenance start time represented as hh , where hh is the hour (00 to 23). The hour of the day is in the time zone of the gateway.
    # minute-of-hour : The minute component of the maintenance start time represented as mm , where mm is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("storagegateway", "update-maintenance-start-time", "gateway-arn", "hour-of-day", "minute-of-hour", add_option_dict)
