#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-notification-channel.html
if __name__ == '__main__':
    """
	add-notification-channels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/add-notification-channels.html
    """

    parameter_display_string = """
    # channel-id : The id of the channel that we want to stop receiving notifications.
    # profiling-group-name : The name of the profiling group we want to change notification configuration for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeguruprofiler", "remove-notification-channel", "channel-id", "profiling-group-name", add_option_dict)
