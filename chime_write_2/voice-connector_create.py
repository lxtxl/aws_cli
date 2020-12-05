#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-voice-connector.html
if __name__ == '__main__':
    """
	delete-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector.html
	get-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector.html
	list-voice-connectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connectors.html
	update-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-voice-connector.html
    """

    parameter_display_string = """
    # name : The name of the Amazon Chime Voice Connector.
    # require-encryption | --no-require-encryption : When enabled, requires encryption for the Amazon Chime Voice Connector.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "create-voice-connector", "name", "require-encryption | --no-require-encryption", add_option_dict)
