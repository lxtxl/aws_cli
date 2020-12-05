#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-client-vpn-connections.html
if __name__ == '__main__':
    """
	describe-client-vpn-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-connections.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint to which the client is connected.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "terminate-client-vpn-connections", "client-vpn-endpoint-id", add_option_dict)





