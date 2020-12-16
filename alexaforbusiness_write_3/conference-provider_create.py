#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-conference-provider.html
if __name__ == '__main__':
    """
	delete-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-conference-provider.html
	get-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-conference-provider.html
	list-conference-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-conference-providers.html
	update-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-conference-provider.html
    """

    parameter_display_string = """
    # conference-provider-name : The name of the conference provider.
    # conference-provider-type : Represents a type within a list of predefined types.
Possible values:

CHIME
BLUEJEANS
FUZE
GOOGLE_HANGOUTS
POLYCOM
RINGCENTRAL
SKYPE_FOR_BUSINESS
WEBEX
ZOOM
CUSTOM
    # meeting-setting : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("alexaforbusiness", "create-conference-provider", "conference-provider-name", "conference-provider-type", "meeting-setting", add_option_dict)
