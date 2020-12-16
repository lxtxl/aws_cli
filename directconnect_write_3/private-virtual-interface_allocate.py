#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-private-virtual-interface.html
if __name__ == '__main__':
    """
	confirm-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-private-virtual-interface.html
	create-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-private-virtual-interface.html
    """

    parameter_display_string = """
    # connection-id : The ID of the connection on which the private virtual interface is provisioned.
    # owner-account : The ID of the AWS account that owns the virtual private interface.
    # new-private-virtual-interface-allocation : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("directconnect", "allocate-private-virtual-interface", "connection-id", "owner-account", "new-private-virtual-interface-allocation", add_option_dict)
