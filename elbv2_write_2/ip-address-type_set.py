#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-ip-address-type.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # load-balancer-arn : The Amazon Resource Name (ARN) of the load balancer.
    # ip-address-type : The IP address type. The possible values are ipv4 (for IPv4 addresses) and dualstack (for IPv4 and IPv6 addresses). Internal load balancers must use ipv4 .
Possible values:

ipv4
dualstack
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "set-ip-address-type", "load-balancer-arn", "ip-address-type", add_option_dict)
