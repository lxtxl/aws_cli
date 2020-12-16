#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-route.html
if __name__ == '__main__':
    """
	delete-client-vpn-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-route.html
	describe-client-vpn-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-routes.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint to which to add the route.
    # destination-cidr-block : The IPv4 address range, in CIDR notation, of the route destination. For example:

To add a route for Internet access, enter 0.0.0.0/0
To add a route for a peered VPC, enter the peered VPCâs IPv4 CIDR range
To add a route for an on-premises network, enter the AWS Site-to-Site VPN connectionâs IPv4 CIDR range
To add a route for the local network, enter the client CIDR range
    # target-vpc-subnet-id : The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of the Client VPN endpoint.
Alternatively, if youâre adding a route for the local network, specify local .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ec2", "create-client-vpn-route", "client-vpn-endpoint-id", "destination-cidr-block", "target-vpc-subnet-id", add_option_dict)
