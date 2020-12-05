#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association-proposal.html
if __name__ == '__main__':
    """
	accept-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html
	create-direct-connect-gateway-association-proposal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html
	describe-direct-connect-gateway-association-proposals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html
    """

    parameter_display_string = """
    # proposal-id : The ID of the proposal.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("directconnect", "delete-direct-connect-gateway-association-proposal", "proposal-id", add_option_dict)





