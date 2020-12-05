#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-customer-gateway.html
if __name__ == '__main__':
    """
	delete-customer-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-customer-gateway.html
	describe-customer-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-customer-gateways.html
    """

    parameter_display_string = """
    # bgp-asn : For devices that support BGP, the customer gatewayâs BGP ASN.
Default: 65000
    # type : The type of VPN connection that this customer gateway supports (ipsec.1 ).
Possible values:

ipsec.1
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "create-customer-gateway", "bgp-asn", "type", add_option_dict)
