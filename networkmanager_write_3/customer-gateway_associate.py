#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/associate-customer-gateway.html
if __name__ == '__main__':
    """
	disassociate-customer-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/disassociate-customer-gateway.html
    """

    parameter_display_string = """
    # customer-gateway-arn : The Amazon Resource Name (ARN) of the customer gateway. For more information, see Resources Defined by Amazon EC2 .
    # global-network-id : The ID of the global network.
    # device-id : The ID of the device.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("networkmanager", "associate-customer-gateway", "customer-gateway-arn", "global-network-id", "device-id", add_option_dict)
