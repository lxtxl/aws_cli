#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice/create-configuration-set-event-destination.html
if __name__ == '__main__':
    """
	delete-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice/delete-configuration-set-event-destination.html
	get-configuration-set-event-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice/get-configuration-set-event-destinations.html
	update-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice/update-configuration-set-event-destination.html
    """

    parameter_display_string = """
    # configuration-set-name : ConfigurationSetName
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint-sms-voice", "create-configuration-set-event-destination", "configuration-set-name", add_option_dict)




