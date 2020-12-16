#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/describe-global-networks.html
if __name__ == '__main__':
    """
	create-global-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-global-network.html
	delete-global-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-global-network.html
	update-global-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-global-network.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("networkmanager", "describe-global-networks", add_option_dict)