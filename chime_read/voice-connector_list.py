#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connectors.html
if __name__ == '__main__':
    """
	create-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-voice-connector.html
	delete-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector.html
	get-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector.html
	update-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-voice-connector.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("chime", "list-voice-connectors", add_option_dict)