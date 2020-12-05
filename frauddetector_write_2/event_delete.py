#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-event.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # event-id : The ID of the event to delete.
    # event-type-name : The name of the event type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "delete-event", "event-id", "event-type-name", add_option_dict)
