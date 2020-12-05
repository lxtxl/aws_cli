#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-virtual-interface.html
if __name__ == '__main__':
    """
	delete-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-virtual-interface.html
	describe-virtual-interfaces : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-virtual-interfaces.html
    """

    parameter_display_string = """
    # virtual-interface-id : The ID of the virtual interface.
    # connection-id : The ID of the LAG or connection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "associate-virtual-interface", "virtual-interface-id", "connection-id", add_option_dict)
