#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-termination-credentials.html
if __name__ == '__main__':
    """
	list-voice-connector-termination-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connector-termination-credentials.html
	put-voice-connector-termination-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-termination-credentials.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime Voice Connector ID.
    # usernames : The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "delete-voice-connector-termination-credentials", "voice-connector-id", "usernames", add_option_dict)
