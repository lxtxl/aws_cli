#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-connection-with-lag.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # connection-id : The ID of the connection.
    # lag-id : The ID of the LAG with which to associate the connection.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("directconnect", "associate-connection-with-lag", "connection-id", "lag-id", add_option_dict)
