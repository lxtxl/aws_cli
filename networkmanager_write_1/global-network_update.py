#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-global-network.html
if __name__ == '__main__':
    """
	create-global-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-global-network.html
	delete-global-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-global-network.html
	describe-global-networks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/describe-global-networks.html
    """

    parameter_display_string = """
    # global-network-id : The ID of your global network.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("networkmanager", "update-global-network", "global-network-id", add_option_dict)





