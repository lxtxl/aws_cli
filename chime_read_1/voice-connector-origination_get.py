#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-origination.html
if __name__ == '__main__':
    """
	delete-voice-connector-origination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-origination.html
	put-voice-connector-origination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-origination.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime Voice Connector ID.
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

    execute_one_parameter("chime", "get-voice-connector-origination", "voice-connector-id", add_option_dict)