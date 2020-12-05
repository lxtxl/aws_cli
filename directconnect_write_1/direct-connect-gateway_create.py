#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway.html
if __name__ == '__main__':
    """
	delete-direct-connect-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway.html
	describe-direct-connect-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateways.html
    """

    parameter_display_string = """
    # direct-connect-gateway-name : The name of the Direct Connect gateway.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("directconnect", "create-direct-connect-gateway", "direct-connect-gateway-name", add_option_dict)





