#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-transit-virtual-interface.html
if __name__ == '__main__':
    """
	allocate-transit-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-transit-virtual-interface.html
	create-transit-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-transit-virtual-interface.html
    """

    parameter_display_string = """
    # virtual-interface-id : The ID of the virtual interface.
    # direct-connect-gateway-id : The ID of the Direct Connect gateway.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "confirm-transit-virtual-interface", "virtual-interface-id", "direct-connect-gateway-id", add_option_dict)
