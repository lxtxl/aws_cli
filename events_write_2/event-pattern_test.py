#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/test-event-pattern.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # event-pattern : The event pattern. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide .
    # event : The event, in JSON format, to test against the event pattern.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("events", "test-event-pattern", "event-pattern", "event", add_option_dict)
