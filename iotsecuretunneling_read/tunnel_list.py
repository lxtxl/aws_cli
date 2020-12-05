#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/list-tunnels.html
if __name__ == '__main__':
    """
	close-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/close-tunnel.html
	describe-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/describe-tunnel.html
	open-tunnel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/open-tunnel.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iotsecuretunneling", "list-tunnels", add_option_dict)