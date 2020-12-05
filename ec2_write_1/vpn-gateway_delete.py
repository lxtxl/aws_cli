#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-gateway.html
if __name__ == '__main__':
    """
	attach-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html
	create-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html
	describe-vpn-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-gateways.html
	detach-vpn-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html
    """

    parameter_display_string = """
    # vpn-gateway-id : The ID of the virtual private gateway.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-vpn-gateway", "vpn-gateway-id", add_option_dict)





