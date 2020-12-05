#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-route.html
if __name__ == '__main__':
    """
	create-client-vpn-route : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-route.html
	describe-client-vpn-routes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-routes.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint from which the route is to be deleted.
    # destination-cidr-block : The IPv4 address range, in CIDR notation, of the route to be deleted.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "delete-client-vpn-route", "client-vpn-endpoint-id", "destination-cidr-block", add_option_dict)
