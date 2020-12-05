#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-gateway.html
if __name__ == '__main__':
    """
	delete-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-gateway.html
	describe-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway.html
	list-gateways : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-gateways.html
	update-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-gateway.html
    """

    parameter_display_string = """
    # gateway-name : A unique, friendly name for the gateway.
    # gateway-platform : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotsitewise", "create-gateway", "gateway-name", "gateway-platform", add_option_dict)
