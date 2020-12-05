#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-partner-event-source.html
if __name__ == '__main__':
    """
	delete-partner-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-partner-event-source.html
	describe-partner-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-partner-event-source.html
	list-partner-event-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-partner-event-sources.html
    """

    parameter_display_string = """
    # name : The name of the partner event source. This name must be unique and must be in the format `` partner_name /event_namespace /event_name `` . The AWS account that wants to use this partner event source must create a partner event bus with a name that matches the name of the partner event source.
    # account : The AWS account ID that is permitted to create a matching partner event bus for this partner event source.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("events", "create-partner-event-source", "name", "account", add_option_dict)
