#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-configuration-set-event-destinations.html
if __name__ == '__main__':
    """
	create-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-configuration-set-event-destination.html
	delete-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/delete-configuration-set-event-destination.html
	update-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/update-configuration-set-event-destination.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that contains the event destination.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("sesv2", "get-configuration-set-event-destinations", "configuration-set-name", add_option_dict)