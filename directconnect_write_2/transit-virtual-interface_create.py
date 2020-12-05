#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-transit-virtual-interface.html
if __name__ == '__main__':
    """
	allocate-transit-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-transit-virtual-interface.html
	confirm-transit-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-transit-virtual-interface.html
    """

    parameter_display_string = """
    # connection-id : The ID of the connection.
    # new-transit-virtual-interface : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "create-transit-virtual-interface", "connection-id", "new-transit-virtual-interface", add_option_dict)
