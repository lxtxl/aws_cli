#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-configuration-set-event-destination.html
if __name__ == '__main__':
    """
	delete-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-configuration-set-event-destination.html
	update-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-configuration-set-event-destination.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that the event destination should be associated with.
    # event-destination : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ses", "create-configuration-set-event-destination", "configuration-set-name", "event-destination", add_option_dict)
