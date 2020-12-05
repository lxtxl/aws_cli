#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-retention-policy.html
if __name__ == '__main__':
    """
	delete-retention-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-retention-policy.html
    """

    parameter_display_string = """
    # log-group-name : The name of the log group.
    # retention-in-days : The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.
If you omit retentionInDays in a PutRetentionPolicy operation, the events in the log group are always retained and never expire.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("logs", "put-retention-policy", "log-group-name", "retention-in-days", add_option_dict)
