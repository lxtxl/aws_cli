#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html
if __name__ == '__main__':
    """
	delete-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection.html
	describe-vpn-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html
	modify-vpn-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html
    """

    parameter_display_string = """
    # customer-gateway-id : The ID of the customer gateway.
    # type : The type of VPN connection (ipsec.1 ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-vpn-connection", "customer-gateway-id", "type", add_option_dict)
