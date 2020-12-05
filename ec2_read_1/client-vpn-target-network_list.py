#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-target-networks.html
if __name__ == '__main__':
    """
	associate-client-vpn-target-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-client-vpn-target-network.html
	disassociate-client-vpn-target-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-client-vpn-target-network.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint.
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

    execute_one_parameter("ec2", "describe-client-vpn-target-networks", "client-vpn-endpoint-id", add_option_dict)