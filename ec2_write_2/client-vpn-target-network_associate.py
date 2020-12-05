#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-client-vpn-target-network.html
if __name__ == '__main__':
    """
	describe-client-vpn-target-networks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-target-networks.html
	disassociate-client-vpn-target-network : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-client-vpn-target-network.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint.
    # subnet-id : The ID of the subnet to associate with the Client VPN endpoint.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "associate-client-vpn-target-network", "client-vpn-endpoint-id", "subnet-id", add_option_dict)
