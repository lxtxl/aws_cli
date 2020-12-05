#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-private-virtual-interface.html
if __name__ == '__main__':
    """
	allocate-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-private-virtual-interface.html
	confirm-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-private-virtual-interface.html
    """

    parameter_display_string = """
    # connection-id : The ID of the connection.
    # new-private-virtual-interface : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "create-private-virtual-interface", "connection-id", "new-private-virtual-interface", add_option_dict)
