#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-configuration-set-event-destination.html
if __name__ == '__main__':
    """
	create-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-configuration-set-event-destination.html
	delete-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-configuration-set-event-destination.html
	get-configuration-set-event-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-configuration-set-event-destinations.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that contains the event destination that you want to modify.
    # event-destination-name : The name of the event destination that you want to modify.
    # event-destination : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sesv2", "update-configuration-set-event-destination", "configuration-set-name", "event-destination-name", "event-destination", add_option_dict)
