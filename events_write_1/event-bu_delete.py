#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-event-bus.html
if __name__ == '__main__':
    """
	create-event-bus : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-event-bus.html
	describe-event-bus : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-event-bus.html
    """

    parameter_display_string = """
    # name : The name of the event bus to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "delete-event-bus", "name", add_option_dict)





