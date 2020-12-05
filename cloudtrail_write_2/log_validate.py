#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/validate-logs.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # trail-arn : Specifies the ARN of the trail to be validated
    # start-time : Specifies that log files delivered on or after the specified UTC timestamp value will be validated. Example: â2015-01-08T05:21:42Zâ.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudtrail", "validate-logs", "trail-arn", "start-time", add_option_dict)
