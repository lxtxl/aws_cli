#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-streaming-configuration.html
if __name__ == '__main__':
    """
	delete-voice-connector-streaming-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-streaming-configuration.html
	get-voice-connector-streaming-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-streaming-configuration.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime Voice Connector ID.
    # streaming-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "put-voice-connector-streaming-configuration", "voice-connector-id", "streaming-configuration", add_option_dict)
