#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-streaming-configuration.html
if __name__ == '__main__':
    """
	get-voice-connector-streaming-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-streaming-configuration.html
	put-voice-connector-streaming-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-streaming-configuration.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime Voice Connector ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-voice-connector-streaming-configuration", "voice-connector-id", add_option_dict)





