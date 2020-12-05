#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/describe-handshake.html
if __name__ == '__main__':
    """
	accept-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/accept-handshake.html
	cancel-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/cancel-handshake.html
	decline-handshake : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/decline-handshake.html
    """

    parameter_display_string = """
    # handshake-id : The unique identifier (ID) of the handshake that you want information about. You can get the ID from the original call to  InviteAccountToOrganization , or from a call to  ListHandshakesForAccount or  ListHandshakesForOrganization .
The regex pattern for handshake ID string requires âh-â followed by from 8 to 32 lowercase letters or digits.
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

    execute_one_parameter("organizations", "describe-handshake", "handshake-id", add_option_dict)