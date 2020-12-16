#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-proxy-session.html
if __name__ == '__main__':
    """
	delete-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-proxy-session.html
	get-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-proxy-session.html
	list-proxy-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-proxy-sessions.html
	update-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-proxy-session.html
    """

    parameter_display_string = """
    # voice-connector-id : The Amazon Chime voice connector ID.
    # participant-phone-numbers : The participant phone numbers.
(string)
    # capabilities : The proxy session capabilities.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("chime", "create-proxy-session", "voice-connector-id", "participant-phone-numbers", "capabilities", add_option_dict)
