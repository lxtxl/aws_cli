#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-hosted-connection.html
if __name__ == '__main__':
    """
	allocate-hosted-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-hosted-connection.html
	describe-hosted-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-hosted-connections.html
    """

    parameter_display_string = """
    # connection-id : The ID of the hosted connection.
    # parent-connection-id : The ID of the interconnect or the LAG.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "associate-hosted-connection", "connection-id", "parent-connection-id", add_option_dict)
