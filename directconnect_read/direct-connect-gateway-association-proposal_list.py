#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html
if __name__ == '__main__':
    """
	accept-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html
	create-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html
	delete-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("directconnect", "describe-direct-connect-gateway-association-proposals", add_option_dict)