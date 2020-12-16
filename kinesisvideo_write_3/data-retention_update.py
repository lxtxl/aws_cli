#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/update-data-retention.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # current-version : The version of the stream whose retention period you want to change. To get the version, call either the DescribeStream or the ListStreams API.
    # operation : Indicates whether you want to increase or decrease the retention period.
Possible values:

INCREASE_DATA_RETENTION
DECREASE_DATA_RETENTION
    # data-retention-change-in-hours : The retention period, in hours. The value you specify replaces the current value. The maximum value for this parameter is 87600 (ten years).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesisvideo", "update-data-retention", "current-version", "operation", "data-retention-change-in-hours", add_option_dict)
