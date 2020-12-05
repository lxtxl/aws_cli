#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-client-vpn-ingress.html
if __name__ == '__main__':
    """
	revoke-client-vpn-ingress : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-client-vpn-ingress.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint.
    # target-network-cidr : The IPv4 address range, in CIDR notation, of the network for which access is being authorized.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "authorize-client-vpn-ingress", "client-vpn-endpoint-id", "target-network-cidr", add_option_dict)
