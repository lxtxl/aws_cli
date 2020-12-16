#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html
if __name__ == '__main__':
    """
	accept-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html
	delete-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html
	describe-direct-connect-gateway-association-proposals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html
    """

    parameter_display_string = """
    # direct-connect-gateway-id : The ID of the Direct Connect gateway.
    # direct-connect-gateway-owner-account : The ID of the AWS account that owns the Direct Connect gateway.
    # gateway-id : The ID of the virtual private gateway or transit gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("directconnect", "create-direct-connect-gateway-association-proposal", "direct-connect-gateway-id", "direct-connect-gateway-owner-account", "gateway-id", add_option_dict)
