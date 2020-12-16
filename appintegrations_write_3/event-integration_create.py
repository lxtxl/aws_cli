#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/create-event-integration.html
if __name__ == '__main__':
    """
	delete-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/delete-event-integration.html
	get-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/get-event-integration.html
	list-event-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/list-event-integrations.html
	update-event-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appintegrations/update-event-integration.html
    """

    parameter_display_string = """
    # name : The name of the event integration.
    # event-filter : 
    # event-bridge-bus : The Eventbridge bus.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("appintegrations", "create-event-integration", "name", "event-filter", "event-bridge-bus", add_option_dict)
