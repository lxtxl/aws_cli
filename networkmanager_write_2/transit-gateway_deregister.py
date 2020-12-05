#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/deregister-transit-gateway.html
if __name__ == '__main__':
    """
	register-transit-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/register-transit-gateway.html
    """

    parameter_display_string = """
    # global-network-id : The ID of the global network.
    # transit-gateway-arn : The Amazon Resource Name (ARN) of the transit gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("networkmanager", "deregister-transit-gateway", "global-network-id", "transit-gateway-arn", add_option_dict)
