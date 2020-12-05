#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-event-bus.html
if __name__ == '__main__':
    """
	delete-event-bus : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-event-bus.html
	describe-event-bus : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-event-bus.html
    """

    parameter_display_string = """
    # name : The name of the new event bus.
Event bus names cannot contain the / character. You canât use the name default for a custom event bus, as this name is already used for your accountâs default event bus.
If this is a partner event bus, the name must exactly match the name of the partner event source that this event bus is matched to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("events", "create-event-bus", "name", add_option_dict)





