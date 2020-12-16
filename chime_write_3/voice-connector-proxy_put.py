#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-proxy.html
if __name__ == '__main__':
    """
	delete-voice-connector-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-proxy.html
	get-voice-connector-proxy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-proxy.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime voice connector ID.
    # default-session-expiry-minutes : The default number of minutes allowed for proxy sessions.
    # phone-number-pool-countries : The countries for proxy phone numbers to be selected from.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "put-voice-connector-proxy", "voice-connector-id", "default-session-expiry-minutes", "phone-number-pool-countries", add_option_dict)
