#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-voice-connector-group.html
if __name__ == '__main__':
    """
	create-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-voice-connector-group.html
	delete-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-group.html
	get-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-group.html
	list-voice-connector-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connector-groups.html
    """

    parameter_display_string = """
    # voice-connector-group-id : The Amazon Chime Voice Connector group ID.
    # name : The name of the Amazon Chime Voice Connector group.
    # voice-connector-items : The VoiceConnectorItems to associate with the group.
(structure)

For Amazon Chime Voice Connector groups, the Amazon Chime Voice Connectors to which to route inbound calls. Includes priority configuration settings. Limit: 3 VoiceConnectorItems per Amazon Chime Voice Connector group.
VoiceConnectorId -> (string)

The Amazon Chime Voice Connector ID.

Priority -> (integer)

The priority associated with the Amazon Chime Voice Connector, with 1 being the highest priority. Higher priority Amazon Chime Voice Connectors are attempted first.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "update-voice-connector-group", "voice-connector-group-id", "name", "voice-connector-items", add_option_dict)
