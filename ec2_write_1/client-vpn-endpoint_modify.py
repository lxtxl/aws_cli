#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-client-vpn-endpoint.html
if __name__ == '__main__':
    """
	create-client-vpn-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-endpoint.html
	delete-client-vpn-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-endpoint.html
	describe-client-vpn-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-endpoints.html
    """

    parameter_display_string = """
    # client-vpn-endpoint-id : The ID of the Client VPN endpoint to modify.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "modify-client-vpn-endpoint", "client-vpn-endpoint-id", add_option_dict)





