#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/associate-phone-numbers-with-voice-connector-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # voice-connector-group-id : The Amazon Chime Voice Connector group ID.
    # e164-phone-numbers : List of phone numbers, in E.164 format.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "associate-phone-numbers-with-voice-connector-group", "voice-connector-group-id", "e164-phone-numbers", add_option_dict)
