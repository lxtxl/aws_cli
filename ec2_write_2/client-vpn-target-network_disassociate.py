#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-client-vpn-target-network.html
if __name__ == '__main__':
    """
	associate-client-vpn-target-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-client-vpn-target-network.html
	describe-client-vpn-target-networks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-target-networks.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint from which to disassociate the target network.
    # association-id : The ID of the target network association.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "disassociate-client-vpn-target-network", "client-vpn-endpoint-id", "association-id", add_option_dict)
