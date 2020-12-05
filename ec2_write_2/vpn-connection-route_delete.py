#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection-route.html
if __name__ == '__main__':
    """
	create-vpn-connection-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection-route.html
    """

    parameter_display_string = """
    # destination-cidr-block : The CIDR block associated with the local subnet of the customer network.
    # vpn-connection-id : The ID of the VPN connection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "delete-vpn-connection-route", "destination-cidr-block", "vpn-connection-id", add_option_dict)
