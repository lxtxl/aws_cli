#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html
if __name__ == '__main__':
    """
	close-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/close-tunnel.html
	list-tunnels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/list-tunnels.html
	open-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/open-tunnel.html
    """

    parameter_display_string = """
    # tunnel-id : The tunnel to describe.
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

    execute_one_parameter("iotsecuretunneling", "describe-tunnel", "tunnel-id", add_option_dict)