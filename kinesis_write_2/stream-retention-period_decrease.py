#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/decrease-stream-retention-period.html
if __name__ == '__main__':
    """
	increase-stream-retention-period : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/increase-stream-retention-period.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream to modify.
    # retention-period-hours : The new retention period of the stream, in hours. Must be less than the current retention period.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "decrease-stream-retention-period", "stream-name", "retention-period-hours", add_option_dict)
