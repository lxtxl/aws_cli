#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-tunnel-certificate.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # vpn-connection-id : The ID of the AWS Site-to-Site VPN connection.
    # vpn-tunnel-outside-ip-address : The external IP address of the VPN tunnel.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "modify-vpn-tunnel-certificate", "vpn-connection-id", "vpn-tunnel-outside-ip-address", add_option_dict)
